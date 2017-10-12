import os
import subprocess
import datetime
import threading
from config_reader import AppConfigReader
from pony.orm import db_session
from database import db, Job


class JobManager:

    def __init__(self, id_job, email=None, fasta_q=None, fasta_t=None, query_name=None, target_name=None):
        self.id_job = id_job
        self.email = email
        self.fasta_q = fasta_q
        self.fasta_t = fasta_t
        self.query = query_name
        self.target = target_name
        config_reader = AppConfigReader()
        # Get configs:
        self.batch_system_type = config_reader.get_batch_system_type()
        self.minimap2 = config_reader.get_minimap2_exec()
        self.samtools = config_reader.get_samtools_exec()
        self.threads = config_reader.get_nb_threads()
        self.app_data = config_reader.get_app_data()
        # Outputs:
        self.output_dir = os.path.join(self.app_data, id_job)
        self.paf_raw = os.path.join(self.output_dir, "map_raw.paf")
        self.paf = os.path.join(self.output_dir, "map.paf")
        self.idx_q = os.path.join(self.output_dir, "query.idx")
        self.idx_t = os.path.join(self.output_dir, "target.idx")
        self.logs = os.path.join(self.output_dir, "logs.txt")

    def __check_job_success_local(self):
        if os.path.exists(self.paf):
            if os.path.getsize(self.paf) > 0:
                if os.path.exists(self.idx_q):
                    if os.path.getsize(self.idx_q) > 0:
                        if os.path.exists(self.idx_t):
                            if os.path.getsize(self.idx_t) > 0:
                                return "success"
        return "error"

    def check_job_success(self):
        if self.batch_system_type == "local":
            return self.__check_job_success_local()

    @db_session
    def __launch_local(self):
        cmd = ["run_minimap2.sh", self.minimap2, self.samtools, self.threads, self.fasta_t, self.fasta_q, self.query,
               self.target, self.paf_raw, self.paf]
        with open(self.logs, "w") as logs:
            p = subprocess.Popen(cmd, stdout=logs, stderr=logs)
        job = Job.get(id_job=self.id_job)
        job.id_process = p.pid
        job.status = "started"
        db.commit()
        p.wait()
        status = self.check_job_success()
        job.status = status
        db.commit()

    @db_session
    def launch(self):
        job = Job(id_job=self.id_job, email=self.email, batch_type=self.batch_system_type,
                  date_created=datetime.datetime.now())
        db.commit()
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)
        if self.batch_system_type == "local":
            thread = threading.Timer(1, self.__launch_local)
            thread.start()

    @db_session
    def status(self):
        job = Job.get(id_job=self.id_job)
        if job is not None:
            return job.status
        else:
            return "unknown"
