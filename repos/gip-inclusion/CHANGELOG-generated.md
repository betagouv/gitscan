# Synthèse d'activité : gip-inclusion (du 20/06 au 13/08)

## Résumé de l'activité
L'activité de la période est marquée par des évolutions majeures de l'expérience utilisateur et de l'offre fonctionnelle. Le rebranding de l'outil EURES en "Match Europe" [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) et la refonte complète de la page d'accueil [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) marquent des étapes clés. 

L'intégration du module d'orientation dans [les-emplois](/repos/gip-inclusion/les-emplois), le déploiement d'un pipeline complet pour les emails SPS [sps-emailer](/repos/gip-inclusion/sps-emailer) et l'amélioration des capacités de recherche et de pilotage ([dora](/repos/gip-inclusion/dora), [data-inclusion](/repos/gip-inclusion/data-inclusion), [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow)) renforcent l'impact des outils pour les acteurs de l'inclusion et les décideurs.

## Sécurité
- Refonte complète de la double authentification (MFA) pour renforcer la sécurité des accès [les-emplois](/repos/gip-inclusion/les-emplois).
- Mise en place de l'authentification par jeton (token authentication) [api-relay-cnav](/repos/gip-inclusion/api-relay-cnav).
- Amélioration de la confidentialité via l'anonymisation automatique des données sensibles [autometa](/repos/gip-inclusion/autometa).
- Sécurisation des accès aux téléchargements [le-marche](/repos/gip-inclusion/le-marche) et suppression des mots de passe codés en dur dans les prototypes [fluo-proto](/repos/gip-inclusion/fluo-proto).
- Correction de vulnérabilités [immersion-facile](/repos/gip-inclusion/immersion-facile).

## Autres changements notables
- Migration vers une architecture Django complète et conteneurisée [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil).
- Passage à un modèle de déploiement serverless pour les prototypes [fluo-proto](/repos/gip-inclusion/fluo-proto).
- Refonte profonde de l'architecture des données et des modèles d'inclusion [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) et [dora](/repos/gip-inclusion/dora).

## Dépôts les plus actifs
- [les-emplois](/repos/gip-inclusion/les-emplois) : Intégration du module d'orientation, refonte de la sécurité (MFA) et optimisations de performance.
- [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) : Rebranding en Match Europe et gestion complète des candidatures spontanées.
- [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) : Refonte visuelle et migration vers une architecture Django.
- [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) : Enrichissement des tableaux de bord et restructuration de l'architecture de données.
- [dora](/repos/gip-inclusion/dora) : Amélioration de la recherche et migration du référentiel des publics.
