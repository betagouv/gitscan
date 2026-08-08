# Synthèse d'activité : gip-inclusion (du 30/06 au 06/08)

## Résumé de l'activité
L'activité de la période est marquée par des avancées majeures dans l'accompagnement des parcours professionnels et l'enrichissement des outils de pilotage. Le déploiement du module d'orientation dans [les-emplois](/repos/gip-inclusion/les-emplois) et l'amélioration des fonctionnalités de matching EURES dans [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) et [eures-beta](/repos/gip-inclusion/eures-beta) renforcent l'efficacité des mises en relation pour les candidats. 

Parallèlement, la refonte de la [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) et l'optimisation des tableaux de bord dans [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) et [dora](/repos/gip-inclusion/dora) offrent une meilleure visibilité et une expérience utilisateur plus fluide pour les décideurs et les professionnels. Ces évolutions visent à transformer la donnée en un levier de décision plus précis et accessible.

## Sécurité
- **Protection des données personnelles** : Mise en place de la double authentification (2FA/TOTP) dans [les-emplois](/repos/gip-inclusion/les-emplois) et anonymisation automatique des numéros NIR dans les tickets Zendesk via [autometa](/repos/gip-inclusion/autometa).
- **Contrôle des accès et des flux** : Restriction du téléchargement de listes de recherche aux utilisateurs authentifiés dans [le-marche](/repos/gip-inclusion/le-marche) et implémentation d'une politique de sécurité de contenu (CSP) ainsi que d'une authentification par token dans [api-relay-cnav](/repos/gip-inclusion/api-relay-cnav).
- **Sécurisation des infrastructures** : Suppression des mots de passe codés en dur dans [fluo-proto](/repos/gip-inclusion/fluo-proto) et correction de vulnérabilités dans [immersion-facile](/repos/gip-inclusion/immersion-facile).

## Autres changements notables
- **Modernisation des architectures** : Passage au déploiement de conteneurs serverless pour les prototypes dans [fluo-proto](/repos/gip-inclusion/fluo-proto), refonte complète de la [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) (utilisation de Django et mise en place de CI/CD), et restructuration des modèles de données autour de tables de dimensions dans [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow).
- **Optimisation de l'intelligence et des performances** : Amélioration de la recherche sémantique et de la tolérance aux fautes de frappe dans [data-inclusion](/repos/gip-inclusion/data-inclusion), intégration d'embeddings pour l'analyse par IA dans [autometa](/repos/gip-inclusion/autometa), et optimisation des requêtes SQL pour améliorer la réactivité dans [les-emplois](/repos/gip-inclusion/les-emplois) et [immersion-facile](/repos/gip-inclusion/immersion-facile).
- **Développement de nouveaux services** : Initialisation de l'infrastructure SSO avec [authentik-sso](/repos/gip-inclusion/authentik-sso) et mise en place des fondations de l'API dans [api-relay-cnav](/repos/gip-inclusion/api-relay-cnav).

## Dépôts les plus actifs
- [les-emplois](/repos/gip-inclusion/les-emplois) : Déploiement du module d'orientation, renforcement de la sécurité (2FA) et optimisation des performances.
- [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) : Refonte complète de l'interface utilisateur et de l'architecture technique (Django, Docker, CI/CD).
- [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) : Enrichissement massif des indicateurs de pilotage et restructuration de l'architecture de données.
- [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) : Évolutions majeures des formulaires EURES et du système de matching.
- [rdv-insertion](/repos/gip-inclusion/rdv-insertion) : Améliorations de la performance de l'indexation et corrections de bugs fonctionnels.
- [le-marche](/repos/gip-inclusion/le-marche) : Amélioration de l'expérience acheteur et renforcement de la sécurité des données.
