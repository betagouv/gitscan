# Synthèse d'activité : gip-inclusion (du 22/06 au 30/07)

## Résumé de l'activité
L'activité de l'organisation gip-inclusion au cours des dernières semaines a été particulièrement riche, avec des améliorations significatives sur plusieurs fronts. Les efforts se sont concentrés sur l'amélioration de l'expérience utilisateur, notamment sur [le-marche](/repos/gip-inclusion/le-marche) avec l'ajout de fonctionnalités pour les acheteurs et sur [immersion-facile](/repos/gip-inclusion/immersion-facile) avec une refonte du tableau de bord.  Des avancées importantes ont également été réalisées sur l'infrastructure et l'automatisation, avec la mise en place de CI/CD, de linters et de Dependabot sur plusieurs dépôts ([plateforme-accueil](/repos/gip-inclusion/plateforme-accueil), [sps-emailer](/repos/gip-inclusion/sps-emailer), [slash-visio](/repos/gip-inclusion/slash-visio), [fluo-proto](/repos/gip-inclusion/fluo-proto), [autometa-jobs](/repos/gip-inclusion/autometa-jobs)).  Enfin, des efforts considérables ont été consacrés à l'intégration de nouvelles sources de données et à l'amélioration de la qualité des données sur [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) et [data-inclusion](/repos/gip-inclusion/data-inclusion).

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- [le-marche](/repos/gip-inclusion/le-marche) : le téléchargement de listes de recherche est désormais restreint aux utilisateurs authentifiés.
- [authentik-sso](/repos/gip-inclusion/authentik-sso) : ajout d'une configuration de Content Security Policy (CSP).
- [autometa](/repos/gip-inclusion/autometa) : mise à jour de Pillow pour corriger des vulnérabilités.

## Autres changements notables
- [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) : refonte complète de l'architecture et migration vers Django, avec mise en place d'un pipeline CI/CD.
- [sps-emailer](/repos/gip-inclusion/sps-emailer) : implémentation d'un pipeline complet pour les emails SPS, incluant la conversion, l'anonymisation, le rendu et l'envoi via Brevo.
- [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) : intégration de nouvelles sources de données (FAGERH, RDV-I, Dora, Matomo, IMER) et refonte des modèles de données.
- [api-relay-cnav](/repos/gip-inclusion/api-relay-cnav) : mise en place de l'authentification par token et de la structure de base de l'API.

## Dépôts les plus actifs
- [rdv-insertion](/repos/gip-inclusion/rdv-insertion) : Amélioration des performances, correction de bugs et ajout de nouvelles fonctionnalités pour faciliter le suivi des parcours d'accompagnement.
- [le-marche](/repos/gip-inclusion/le-marche) : Amélioration de l'expérience utilisateur pour les acheteurs avec de nouvelles fonctionnalités et corrections.
- [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) : Intégration de nouvelles sources de données et amélioration de la qualité des données.
- [immersion-facile](/repos/gip-inclusion/immersion-facile) : Refonte du tableau de bord et ajout de nouvelles fonctionnalités pour le suivi des conventions.
- [autometa](/repos/gip-inclusion/autometa) : Refonte de la navigation et ajout de nouvelles fonctionnalités d'analyse.
- [dora](/repos/gip-inclusion/dora) : Amélioration de la recherche et de la gestion des services.
