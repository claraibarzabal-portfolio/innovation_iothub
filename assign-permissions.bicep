@description('Nombre del grupo de recursos')
param resourceGroupName string = 'sustentabilidad-grupo7'

@description('Nombre de la Identidad Administrada')
param userAssignedIdentityName string = 'myUserAssignedIdentity'

@description('ID del Azure Data Lake Storage')
param dataLakeStorageId string = '/subscriptions/ef594d88-7488-4b9a-8e8c-ed5075afebb2/resourceGroups/sustentabilidad-grupo7/providers/Microsoft.Storage/storageAccounts/datalakesustentabilidad'

@description('ID del Azure Synapse Analytics')
param synapseId string = '/subscriptions/ef594d88-7488-4b9a-8e8c-ed5075afebb2/resourceGroups/synapseworkspace-managedrg-8a328053-4d89-435c-911d-6189022e2d13/providers/Microsoft.Synapse/workspaces/synapseworkspace-managedrg-8a328053-4d89-435c-911d-6189022e2d13'

@description('ID del Azure Functions')
param functionsId string = '/subscriptions/ef594d88-7488-4b9a-8e8c-ed5075afebb2/resourceGroups/sustentabilidad-grupo7/providers/Microsoft.Web/sites/azure-functions-7'

@description('ID del Azure Bot Service')
param botServiceId string = '/subscriptions/ef594d88-7488-4b9a-8e8c-ed5075afebb2/resourceGroups/sustentabilidad-grupo7/providers/Microsoft.BotService/bot-7'

@description('ID del Azure Machine Learning')
param mlWorkspaceId string = '/subscriptions/ef594d88-7488-4b9a-8e8c-ed5075afebb2/resourceGroups/sustentabilidad-grupo7/providers/Microsoft.MachineLearningServices/workspaces/machine-learning-area-de-trabajo7'

@description('ID del Application Insights')
param insightsId string = '/subscriptions/ef594d88-7488-4b9a-8e8c-ed5075afebb2/resourceGroups/sustentabilidad-grupo7/providers/microsoft.insights/components/azure-functions-7'

resource userAssignedIdentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2018-11-30' existing = {
  name: userAssignedIdentityName
  scope: resourceGroup(resourceGroupName)
}

// Asignar permisos a la identidad administrada en Data Lake
resource roleAssignmentDataLake 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: guid(userAssignedIdentity.id, dataLakeStorageId, 'Storage Blob Data Contributor')
  properties: {
    principalId: userAssignedIdentity.properties.principalId
    roleDefinitionId: subscription().id + '/providers/Microsoft.Authorization/roleDefinitions/' + 'b36bca5e-1ff2-4d5b-a8b0-12728e050d43' // Storage Blob Data Contributor
    scope: dataLakeStorageId
  }
}

// Asignar permisos para Azure Synapse
resource synapseRoleAssignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: guid(userAssignedIdentity.id, synapseId, 'Synapse Contributor')
  properties: {
    principalId: userAssignedIdentity.properties.principalId
    roleDefinitionId: subscription().id + '/providers/Microsoft.Authorization/roleDefinitions/' + '7a123d5d-8d9f-40b0-b5d5-4c456b123456' // Synapse Contributor
    scope: synapseId
  }
}

// Asignar permisos para Azure Functions
resource functionsRoleAssignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: guid(userAssignedIdentity.id, functionsId, 'Azure Functions Contributor')
  properties: {
    principalId: userAssignedIdentity.properties.principalId
    roleDefinitionId: subscription().id + '/providers/Microsoft.Authorization/roleDefinitions/' + 'f4c7c982-8bb6-41be-977e-949f5b9d6c47' // Azure Functions Contributor
    scope: functionsId
  }
}

// Asignar permisos para Azure Bot Service
resource botServiceRoleAssignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: guid(userAssignedIdentity.id, botServiceId, 'Bot Contributor')
  properties: {
    principalId: userAssignedIdentity.properties.principalId
    roleDefinitionId: subscription().id + '/providers/Microsoft.Authorization/roleDefinitions/' + 'c3b0e6a2-7f0b-4703-947e-e5e9c0b67832' // Bot Contributor
    scope: botServiceId
  }
}

// Asignar permisos para Azure Machine Learning
resource mlRoleAssignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: guid(userAssignedIdentity.id, mlWorkspaceId, 'Azure ML Contributor')
  properties: {
    principalId: userAssignedIdentity.properties.principalId
    roleDefinitionId: subscription().id + '/providers/Microsoft.Authorization/roleDefinitions/' + 'f53a7330-0cc4-4e3b-9b2f-6e7480e32a4c' // Azure ML Contributor
    scope: mlWorkspaceId
  }
}

// Asignar permisos para Application Insights
resource insightsRoleAssignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: guid(userAssignedIdentity.id, insightsId, 'Application Insights Component Contributor')
  properties: {
    principalId: userAssignedIdentity.properties.principalId
    roleDefinitionId: subscription().id + '/providers/Microsoft.Authorization/roleDefinitions/' + 'a2e99bb0-4f71-4a5c-b0d3-d78b3b0523b8' // Application Insights Component Contributor
    scope: insightsId
  }
}

