resource "helm_release" "argocd" {
  name  = "argocd"

  repository       = "https://argoproj.github.io/argo-helm"
  chart            = "argo-cd"
  namespace        = "argocd"
  version          = "4.9.7"
  create_namespace = true

    set {
        name = "server.service.type"
        value = "LoadBalancer"
    }
  # values file for argcd where is specified access to app-of-apps
}