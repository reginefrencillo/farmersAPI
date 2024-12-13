from django.db.models.signals import post_migrate
from django.dispatch import receiver
from farmers.models import Barangay, Commodity  # Adjust if your models are located elsewhere

@receiver(post_migrate)
def create_initial_data(sender, **kwargs):
    # List of barangays
    barangays = [
        ('001', 'Balocawe'),
        ('002', 'Banogao'),
        ('003', 'Banuang-Daan'),
        ('004', 'Bariis'),
        ('005', 'Bolo'),
        ('006', 'Bon-Ot Dako'),
        ('007', 'Bon-Ot Saday'),
        ('008', 'Cabagahan'),
        ('009', 'Calayuan'),
        ('010', 'Caloocan (Poblacion)'),
        ('011', 'Calpi'),
        ('012', 'Camachiles (Poblacion)'),
        ('013', 'Camcaman (Poblacion)'),
        ('014', 'Coron-Coron'),
        ('015', 'Culasi'),
        ('016', 'Gadgaran'),
        ('017', 'Genablan-Occidental'),
        ('018', 'Genablan-Oriental'),
        ('019', 'Hid-Hid'),
        ('020', 'Laboy'),
        ('021', 'Lajong'),
        ('022', 'Mambajog'),
        ('023', 'Manjumlao'),
        ('024', 'Manurabi'),
        ('025', 'Nasuracan'),
        ('026', 'Paghuliran'),
        ('027', 'Pange'),
        ('028', 'Pawa'),
        ('029', 'Poropandan'),
        ('030', 'Santa Isabel'),
        ('031', 'Sinalmacan'),
        ('032', 'Sinang-atan'),
        ('033', 'Sinebaran'),
        ('034', 'Sisigon'),
        ('035', 'Suwa'),
        ('036', 'Sulangan'),
        ('037', 'Tablac (Poblacion)'),
        ('038', 'Tabunan (Poblacion)'),
        ('039', 'Tugas'),
    ]

    # Create barangays
    for barangay in barangays:
        Barangay.objects.get_or_create(code=barangay[0], name=barangay[1])

    # List of commodities
    commodities = [
        ('Rice Crops', 'Rice Crops'),
        ('Fisheries', 'Fisheries'),
        ('Livestock and Poultry', 'Livestock and Poultry'),
        ('High Value Commercial Crops', 'High Value Commercial Crops'),
    ]

    # Create commodities
    for commodity in commodities:
        Commodity.objects.get_or_create(name=commodity[0])
