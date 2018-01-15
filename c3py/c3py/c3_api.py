from client import Client
#from api import *
from api.ACLManagement import ACLManagement
from api.CloudAccountManagement import CloudAccountManagement
from api.CustomActionManagement import CustomActionManagement
from api.JobManagement import JobManagement
from api.PolicyManagement import PolicyManagement
from api.ActionManagement import ActionManagement
from api.CloudFamilyManagement import CloudFamilyManagement
from api.DeploymentEnvironmentManagement import DeploymentEnvironmentManagement
from api.KeyManagement import KeyManagement
from api.ProjectManagement import ProjectManagement
from api.ActivationProfilesManagement import ActivationProfilesManagement
from api.CloudImageMappingsManagement import CloudImageMappingsManagement
from api.ExportAndImportApplications import ExportAndImportApplications
from api.LogManagement import LogManagement
from api.ReportManagement import ReportManagement
from api.ApplicationManagement import ApplicationManagement
from api.CloudInstanceManagement import CloudInstanceManagement
from api.ExtensionManagement import ExtensionManagement
from api.LogoManagement import LogoManagement
from api.RoleManagement import RoleManagement
from api.CloudManagement import CloudManagement
from api.FavoriteManagement import FavoriteManagement
from api.MailPropertiesManagement import MailPropertiesManagement
from api.ServiceManagement import ServiceManagement
from api.CloudPropertiesManagement import CloudPropertiesManagement
from api.FederatedManagement import FederatedManagement
from api.MarketPlaceManagement import MarketPlaceManagement
from api.TenantManagement import TenantManagement
from api.BundleManagement import BundleManagement
from api.CloudProviderManagement import CloudProviderManagement
from api.GroupManagement import GroupManagement
from api.OperationStatus import OperationStatus
from api.TenantPropertiesManagement import TenantPropertiesManagement
from api.CCOManagement import CCOManagement
from api.CloudRegionManagement import CloudRegionManagement
from api.ImageManagement import ImageManagement
from api.OwnershipManagement import OwnershipManagement
from api.UserManagement import UserManagement
from api.CertificateManagement import CertificateManagement
from api.CloudStorageManagement import CloudStorageManagement
from api.Phasemanagement import Phasemanagement
from api.VMManagement import VMManagement
from api.ContractManagement import ContractManagement
from api.InventoryManagement import InventoryManagement
from api.PlanManagement import PlanManagement


class c3Api(object):
    def __init__(self, address=None, user=None, apiKey=None):
        self.address = address
        self.user = user
        self.apiKey = apiKey
        self.client = Client(self.address, self.user, self.apiKey)

        self.PolicyManagement = PolicyManagement(self.client)
        #self.ACLManagement = ACLManagement(self.client)
        #self.ActivationProfilesManagement = ActivationProfilesManagement(self.client)
        #self.ApplicationManagement = ApplicationManagement(self.client)
        #SELF.ApplicationManagment
        #self.BundleManagement = BundleManagement(self.client)
        #self.LogManagement = LogManagement(self.client)
        self.ACLManagement = ACLManagement(self.client)
        self.ActionManagement = ActionManagement(self.client)
        self.ActivationProfilesManagement = ActivationProfilesManagement(self.client)
        self.ApplicationManagement = ApplicationManagement(self.client)
        self.BundleManagement = BundleManagement(self.client)
        self.CCOManagement = CCOManagement(self.client)
        self.CertificateManagement = CertificateManagement(self.client)
        self.CloudAccountManagement = CloudAccountManagement(self.client)
        self.CloudFamilyManagement = CloudFamilyManagement(self.client)
        self.CloudImageMappingsManagement = CloudImageMappingsManagement(self.client)
        self.CloudInstanceManagement = CloudInstanceManagement(self.client)
        self.CloudManagement = CloudManagement(self.client)
        self.CloudPropertiesManagement = CloudPropertiesManagement(self.client)
        self.CloudProviderManagement = CloudProviderManagement(self.client)
        self.CloudRegionManagement = CloudRegionManagement(self.client)
        self.CloudStorageManagement = CloudStorageManagement(self.client)
        self.ContractManagement = ContractManagement(self.client)
        self.CustomActionManagement = CustomActionManagement(self.client)
        self.DeploymentEnvironmentManagement = DeploymentEnvironmentManagement(self.client)
        self.ExportAndImportApplications = ExportAndImportApplications(self.client)
        #self.ExtensionManagement = ExtensionManagement(self.client)
        self.FavoriteManagement = FavoriteManagement(self.client)
        self.FederatedManagement = FederatedManagement(self.client)
        self.GroupManagement = GroupManagement(self.client)
        self.ImageManagement = ImageManagement(self.client)
        self.InventoryManagement = InventoryManagement(self.client)
        self.JobManagement = JobManagement(self.client)
        self.KeyManagement = KeyManagement(self.client)
        self.LogManagement = LogManagement(self.client)
        self.LogoManagement = LogoManagement(self.client)
        #self.MailPropertiesManagement = MailPropertiesManagement(self.client)
        #self.MarketPlacemanagement = MarketPlacemanagement(self.client)
        self.OperationStatus = OperationStatus(self.client)
        self.Phasemanagement = Phasemanagement(self.client)
        self.OwnershipManagement = OwnershipManagement(self.client)
        self.PlanManagement = PlanManagement(self.client)
        self.PolicyManagement = PolicyManagement(self.client)
        self.ProjectManagement = ProjectManagement(self.client)
        self.ReportManagement = ReportManagement(self.client)
        self.RoleManagement = RoleManagement(self.client)
        self.ServiceManagement = ServiceManagement(self.client)
        self.TenantManagement = TenantManagement(self.client)
        #self.TenantPropertiesManagement = TenantPropertiesManagement(self.client)
        #self.uploadLogo = uploadLogo(self.client)
        self.UserManagement = UserManagement(self.client)
        self.VMManagement = VMManagement(self.client)
