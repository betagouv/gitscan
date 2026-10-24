# Synthèse d'activité : france-connect (du 11/05 au 18/05)

## Résumé de l'activité
L'activité récente de FranceConnect s'est concentrée sur l'amélioration de l'expérience utilisateur et l'élargissement des capacités de connexion. Les évolutions majeures concernent l'optimisation du tableau de bord, notamment pour une utilisation mobile plus fluide et une meilleure gestion des sessions, ainsi que l'intégration de nouveaux partenaires comme l'IdP Yris [sources](/repos/france-connect/sources). L'assistance aux utilisateurs est également renforcée par l'ajout de liens de support contextuels sur les pages d'erreur [sources](/repos/france-connect/sources).

## Sécurité
- Renforcement de l'isolation réseau par la séparation des consommateurs de données MongoDB selon le niveau d'assurance (faible ou élevé) [sources](/repos/france-connect/sources).
- Amélioration de la protection des données privées via la suppression de champs d'information inutilisés ("phone_number" et "address") dans FranceConnect+ [sources](/repos/france-connect/sources).

## Autres changements notables
- Évolutions techniques majeures incluant la migration vers `react-router-dom` v6 et une refactorisation de l'architecture des dossiers pour optimiser le partage de code entre les applications [sources](/repos/france-connect/sources).
- Amélioration de la traçabilité et du diagnostic grâce à l'implémentation de logs métier détaillés (incluant l'IP et le port client) et au renforcement des tests automatisés (BDD) [sources](/repos/france-connect/sources).

## Dépôts les plus actifs
- [sources](/repos/france-connect/sources) : Améliorations de l'interface utilisateur, renforcement de l'isolation réseau et optimisation de la traçabilité technique.
