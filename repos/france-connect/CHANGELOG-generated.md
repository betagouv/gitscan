# Synthèse d'activité : france-connect (du 11/05 au 18/05)

## Résumé de l'activité
L'activité de la période a été principalement orientée vers l'amélioration de l'expérience utilisateur et l'élargissement de l'écosystème. Des optimisations ont été apportées au tableau de bord, notamment pour une utilisation mobile plus fluide et une meilleure gestion des sessions, ainsi que l'ajout de liens de support contextuels pour faciliter l'assistance en cas d'erreur. Par ailleurs, l'ouverture vers des prestataires ayant des exigences de sécurité différentes via l'eIDASBridge et l'intégration de nouveaux éléments visuels pour les futurs partenaires renforcent la capacité d'accueil de la plateforme [sources](/repos/france-connect/sources).

## Sécurité
- Amélioration de l'isolation réseau par la séparation des consommateurs MongoDB selon les niveaux d'assurance [sources](/repos/france-connect/sources).
- Renforcement de la protection des données personnelles par la suppression de claims inutilisés ("phone_number" et "address") dans FranceConnect+ [sources](/repos/france-connect/sources).

## Autres changements notables
- Refactorisation de l'architecture des dossiers pour optimiser le partage de code entre les différentes applications [sources](/repos/france-connect/sources).
- Amélioration de l'observabilité et du diagnostic grâce à l'implémentation de logs métier détaillés (incluant l'IP et le port client) [sources](/repos/france-connect/sources).
- Renforcement de la qualité logicielle via l'ajout de tests BDD sur les notifications et l'historique de connexion [sources](/repos/france-connect/sources).

## Dépôts les plus actifs
- [sources](/repos/france-connect/sources) : Travaux centrés sur l'optimisation de l'expérience utilisateur, la structuration technique et la traçabilité.
