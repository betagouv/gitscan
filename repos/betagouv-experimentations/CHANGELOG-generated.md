# Synthèse d'activité : betagouv-experimentations (du 13 mai au 26 mai 2026)

## Résumé de l'activité
L'activité de l'organisation au cours des deux dernières semaines a été marquée par le lancement de nombreux nouveaux projets prototypes, souvent en utilisant Coolify pour le déploiement et le Design System Français (DSFR) pour l'interface utilisateur. Plusieurs projets ont progressé au-delà de la phase d'initialisation, notamment [test-jb3](/repos/betagouv-experimentations/test-jb3) qui a bénéficié d'une mise à jour de sécurité critique, et [test-cadrer-20260521](/repos/betagouv-experimentations/test-cadrer-20260521) et [crm-asn](/repos/betagouv-experimentations/crm-asn) qui ont vu l'implémentation de fonctionnalités clés pour la gestion des contacts. Le proxy de logs [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) a également connu des avancées significatives en termes de robustesse et d'intégration avec GitHub.

## Sécurité
Une mise à jour de sécurité importante a été appliquée à [test-jb3](/repos/betagouv-experimentations/test-jb3) pour corriger une vulnérabilité SQL injection de haute sévérité dans `drizzle-orm` et `drizzle-kit`.  Des headers de sécurité ont également été ajoutés à [crm-asn](/repos/betagouv-experimentations/crm-asn) pour renforcer la protection de l'application.

## Autres changements notables
- Le projet [template-proto](/repos/betagouv-experimentations/template-proto) a intégré l'auto-provisionnement Coolify et prépare l'utilisation des skills d'IA d'Etalab.
- Le projet [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) a vu l'ajout d'un webhook GitHub pour nettoyer Coolify lors de la suppression d'un dépôt.

## Dépôts les plus actifs
- [test-jb3](/repos/betagouv-experimentations/test-jb3) : Correction d'une vulnérabilité de sécurité et améliorations de la documentation.
- [test-cadrer-20260521](/repos/betagouv-experimentations/test-cadrer-20260521) et [crm-asn](/repos/betagouv-experimentations/crm-asn) : Développement d'une application de suivi des contacts avec des fonctionnalités d'affichage et de sécurité.
- [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) : Amélioration de la gestion des logs Coolify et intégration avec GitHub.
- [repo-test](/repos/betagouv-experimentations/repo-test) : Implémentation d'une application de liste de tâches avec fonctionnalités CRUD et persistance des données.
