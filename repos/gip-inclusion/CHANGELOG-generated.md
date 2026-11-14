# Synthèse d'activité : gip-inclusion (période récente)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par un renforcement majeur de la sécurité et de la conformité, avec un effort conséquent sur la protection des données personnelles (RGPD) et le durcissement des contrôles d'accès. Parallèlement, les outils de mise en relation et de gestion sémantique s'enrichissent, offrant une expérience utilisateur plus fluide et intelligente, notamment grâce à l'intégration de nouvelles sources de données et de capacités de recherche avancées.

Enfin, l'infrastructure évolue vers une plus grande modernité et résilience, avec des déploiements automatisés sur des architectures Kubernetes et serverless, garantissant une meilleure scalabilité des services.

## Sécurité
- **Protection des données et conformité :** Travaux massifs de sécurisation et de mise en conformité RGPD, incluant la protection contre les failles XSS et IDOR, le masquage des données sensibles et le renforcement de l'authentification dans [le-marche](/repos/gip-inclusion/le-marche).
- **Contrôle des accès et des flux :** Implémentation de mécanismes de limitation de débit (rate limiting), de hachage SHA-256 et de sécurisation des webhooks dans [rdvsp-bridging](/repos/gip-inclusion/rdvsp-bridging), [rdv-insertion](/repos/gip-inclusion/rdv-insertion) et [data-inclusion](/repos/gip-inclusion/data-inclusion).
- **Gestion des secrets et identités :** Optimisation de la gestion des secrets (SOPS), des permissions IAM et de l'authentification centralisée dans [infrastructure](/repos/gip-inclusion/infrastructure) et [authentik-sso](/repos/gip-inclusion/authentik-sso).
- **Durcissement technique :** Suppression des mots de passe codés en dur dans [fluo-proto](/repos/gip-inclusion/fluo-proto) et renforcement de la validation des emails et du 2FA dans [les-emplois](/repos/gip-inclusion/les-emplois).

## Autres changements notables
- **Modernisation de l'infrastructure :** Déploiement complet de nouveaux environnements (Kubernetes, réseaux privés) pour [infrastructure](/repos/gip-inclusion/infrastructure) et passage à des architectures serverless pour [fluo-proto](/repos/gip-inclusion/fluo-proto).
- **Optimisation des données :** Amélioration de la qualité et de l'orchestration des flux de données (DBT) dans [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) et [data-inclusion](/repos/gip-inclusion/data-inclusion).
- **Évolutions technologiques majeures :** Migration vers Python 3.14 et RustFS pour [les-emplois](/repos/gip-inclusion/les-emplois), et montée de version vers Django 6.0 pour [le-marche](/repos/gip-inclusion/le-marche).

## Dépôts les plus actifs
- [le-marche](/repos/gip-inclusion/le-marche) : Travaux majeurs sur la sécurité, la conformité RGPD et la maintenance technique.
- [autometa](/repos/gip-inclusion/autometa) : Évolutions significatives sur la recherche sémantique, l'intégration de nouvelles sources de données et la résilience.
- [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) : Rebranding vers Match Europe et optimisation des processus de matching et de candidatures.
- [relecteur](/repos/gip-inclusion/relecteur) : Automatisation poussée des revues de code et intégration dans les workflows CI/CD.
- [data-inclusion](/repos/gip-inclusion/data-inclusion) : Consolidation des pipelines de données et renforcement de la sécurité des API.
