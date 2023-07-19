"""Hardware reference from PCI Ids"""
from django.db import models


class Vendor(models.Model):
    """Store info about hardware vendor"""
    vendor_id = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.name} ({self.vendor_id})"

    class Meta:
        ordering = ("name", )

class Feature(models.Model):
    """Store info about hardware features"""
    name = models.CharField(max_length=64)
    version = models.CharField(max_length=8, blank=True)
    feature_level = models.CharField(max_length=8, blank=True)

    def __str__(self) -> str:
        feature_level = f" ({self.feature_level})" if self.feature_level else ""
        return f"{self.name} {self.version}{feature_level}"


class Generation(models.Model):
    """Store info about a hardware generation"""
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=64)
    year = models.SmallIntegerField()
    introduced_with = models.CharField(max_length=128)
    features = models.ManyToManyField(Feature)


class Device(models.Model):
    """Store info about devices"""
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=4)
    name = models.CharField(max_length=256, blank=True)
    comment = models.CharField(max_length=256, blank=True)
    generation = models.ForeignKey(Generation, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        name = self.name if self.name else "[UNKOWN]"
        return f"{name} ({self.device_id})"


class Subsystem(models.Model):
    """Store info about a subsystem"""
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    subvendor_id = models.CharField(max_length=4)
    subdevice_id = models.CharField(max_length=32)
    name = models.CharField(max_length=256, blank=True)

    def __str__(self) -> str:
        name = self.name if self.name else "[UNKOWN]"
        return f"{name} ({self.subvendor_id}:{self.subdevice_id})"