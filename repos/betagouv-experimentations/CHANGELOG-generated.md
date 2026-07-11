# Synthèse d'activité : betagouv-experimentations (du 13 mai au 26 mai 2026)

## Résumé de l'activité
L'organisation a connu une période d'intense activité de lancement de nouveaux prototypes et d'amélioration de l'infrastructure existante. Plusieurs nouveaux projets ont été initialisés, notamment `test-jb4`, `test-jb2`, `test-benoit`, `simulation-doctorat`, `eval-metier-rag` et `26052026`, qui visent à simplifier la création d'applications web et de services pour l'administration en utilisant des outils modernes et le Design System Français.  Parallèlement, des améliorations significatives ont été apportées à `coolify-logs-proxy` pour une meilleure gestion des logs et de l'intégration avec GitHub. Le projet `test-cadrer-20260521` (renommé en `crm-asn`) a progressé avec le développement d'une application de suivi des contacts pour l'équipe ASN de la DINUM. Enfin, `test-jb3` et `repo-test` ont bénéficié d'améliorations fonctionnelles et techniques, notamment des corrections de sécurité et l'ajout de fonctionnalités CRUD.

## Sécurité
Une vulnérabilité SQL injection de haute sévérité a été corrigée dans [test-jb3](/repos/betagouv-experimentations/test-jb3) grâce à une mise à jour de `drizzle-orm` et `drizzle-kit`.  Des headers de sécurité ont également été ajoutés à [crm-asn](/repos/betagouv-experimentations/crm-asn) pour renforcer la protection de l'application.

## Autres changements notables
- Le projet [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) a vu l'ajout d'un endpoint pour la récupération des logs, l'implémentation de l'authentification via GitHub et l'intégration d'un webhook pour la suppression des dépôts.
- Le projet [test-cadrer-20260521](/repos/betagouv-experimentations/test-cadrer-20260521) a été renommé en [crm-asn](/repos/betagouv-experimentations/crm-asn).
- Plusieurs projets ont bénéficié de l'initialisation de l'infrastructure Coolify et de la configuration des workflows CI/CD.

## Dépôts les plus actifs
- [crm-asn](/repos/betagouv-experimentations/crm-asn) : Développement d'une application de suivi des contacts pour l'équipe ASN de la DINUM.
- [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) : Amélioration de la gestion des logs et de l'intégration avec GitHub.
- [test-jb3](/repos/betagouv-experimentations/test-jb3) : Correction de vulnérabilités et améliorations de la documentation.
- [repo-test](/repos/betagouv-experimentations/repo-test) : Ajout d'une application de liste de tâches avec fonctionnalités CRUD et persistance des données.
- [test-cadrer-20260521](/repos/betagouv-experimentations/test-cadrer-20260521) : Initialisation et développement initial d'une application de suivi des contacts.
