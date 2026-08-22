# Synthèse d'activité : france-connect (du 11/05 au 18/05)

## Résumé de l'activité
L'activité de la période s'est concentrée sur l'amélioration de l'expérience utilisateur et l'élargissement des capacités de connexion de l'écosystème. Des optimisations significatives ont été apportées au tableau de bord utilisateur, notamment pour une utilisation mobile plus fluide et une meilleure gestion des sessions, ainsi que l'ajout de mécanismes d'assistance directe via les pages d'erreur. L'intégration du futur IdP Yris et l'ouverture via l'eIDASBridge à des prestataires de services aux exigences de sécurité variées marquent une évolution stratégique de l'offre [sources](/repos/france-connect/sources).

## Sécurité
- Renforcement de l'isolation réseau par la séparation des consommateurs MongoDB selon le niveau d'assurance (faible ou élevé) [sources](/repos/france-connect/sources).
- Amélioration de la protection des données personnelles via la suppression de claims inutilisés ("phone_number" et "address") dans FranceConnect+ [sources](/repos/france-connect/sources).

## Autres changements notables
- Refactorisation de l'architecture logicielle pour faciliter le partage de code entre les différentes applications React [sources](/repos/france-connect/sources).
- Amélioration de la capacité de diagnostic et de la traçabilité grâce à l'implémentation de logs métier détaillés (incluant l'IP et le port client) [sources](/repos/france-connect/sources).
- Renforcement de la qualité et de la fiabilité du système par l'ajout de tests BDD sur les notifications de préférences et l'historique de connexion [sources](/repos/france-connect/sources).

## Dépôts les plus actifs
- [sources](/repos/france-connect/sources) : Évolutions majeures sur l'interface utilisateur, la sécurité des données et la structure technique du projet.
