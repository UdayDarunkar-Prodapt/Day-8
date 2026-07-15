from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment
from services.healthcare_system import HealthcareSystem
from data.datastore import datastore
from utils.loggers import get_logger

logger = get_logger("healthcare.main")
system = HealthcareSystem(datastore)

patient1 = Patient(1, "John Doe", 30, "Male", "Flu")
patient2 = Patient(2, "Jane Smith", 25, "Female", "Cold")
doctor1 = Doctor(101, "Dr. Alice", 40, "General")
appointment1 = Appointment(1001, patient1.id, doctor1.id, "2026-07-15 10:00")

system.add_patient(patient1)
system.add_patient(patient2)
system.add_doctor(doctor1)
system.add_appointment(appointment1)

logger.info("Patient 1: %s", system.patient_service.get_patient(1))
logger.info("Doctor 1: %s", system.doctor_service.get_doctor(101))
logger.info("Appointment 1: %s", system.appointment_service.get_appointment(1001))

