# Synthèse d'activité : france-connect (du 11/05 au 18/05)

## Résumé de l'activité
L'activité récente de FranceConnect s'est concentrée sur l'optimisation de l'expérience utilisateur et l'élargissement de l'écosystème de services. Les utilisateurs bénéficient d'une interface plus fluide, notamment sur mobile, et d'un meilleur accompagnement en cas d'erreur grâce à l'ajout de liens de support contextuels. Par ailleurs, l'intégration de nouveaux prestataires via l'eIDASBridge et la préparation de l'arrivée de l'IdP Yris renforcent la diversité et l'accessibilité des services proposés dans [sources](/repos/france-connect/sources).

## Sécurité
- Renforcement de la traçabilité et du diagnostic grâce à l'ajout de logs métier détaillés (incluant l'IP et le port client) dans [sources](/repos/france-connect/sources).
- Amélioration de l'isolation réseau par la séparation des consommateurs MongoDB selon le niveau d'assurance (faible ou élevé) dans [sources](/repos/france-connect/sources).
- Mise en place de mécanismes de prévention, comme l'affichage d'un avertissement lorsque l'utilisateur désactive l'ensemble de ses identifiants, dans [sources](/repos/france-connect/sources).

## Autres changements notables
- Migration majeure vers la version 6 de `react-router-dom` dans [sources](/repos/france-connect/sources).
- Refactorisation de l'architecture des dossiers et des composants pour améliorer la maintenabilité et le partage de code entre les applications React dans [sources](/repos/france-connect/sources).
- Renforcement de la qualité logicielle via l'implémentation de tests BDD (Behavior Driven Development) pour valider les notifications et l'historique de connexion dans [sources](/repos/france-connect/sources).

## Dépôts les plus actifs
- [sources](/repos/france-connect/sources) : Travaux divers portant sur l'amélioration de l'expérience utilisateur, la sécurité et la refactorisation technique de l'infrastructure.
