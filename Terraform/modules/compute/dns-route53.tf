resource "helm_release" "external_dns" {
    name = "external-dns"
    repository = "https://charts.bitnami.com/bitnami"
    chart = "external-dns"
    wait = true
    version = "6.12.0"
    namespace = "default"
    create_namespace = "true"

    set {
        name="provider"
        value=var.dns_provider
    }
    set {
        name="domainFilters[0]"
        value=var.dns_domain
    }
    set {
        name="policy"
        value=var.policy
    }
    set {
        name="registry"
        value=var.registry
    }
    set {
        name="txtOwnerId"
        value=var.owner_id
    }
    set {
        name="interval"
        value=var.interval  
    }
    set {
        name="rbac.create"
        value=var.rbac_create
    }
    set {
        name="rbac.serviceAccountName"
        value=var.service_account_name
    }
    set {
        name="rbac.serviceAccountAnnotations.eks\\.amazonaws\\.com/role-arn"
        value=var.role_arn
    }
}