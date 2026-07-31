## Changelog : hyyypertool (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette version apporte des améliorations à l'interface utilisateur, notamment concernant la gestion des PDF et des motifs de refus. Des corrections ont été apportées pour l'ouverture des PDF des dirigeants d'association et l'édition des motifs de refus. De nombreuses mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la stabilité de l'outil.

### Évolutions fonctionnelles
- Le PDF des dirigeants d'association s'ouvre désormais dans un nouvel onglet, améliorant l'expérience utilisateur. ([#1746](https://github.com/proconnect-gouv/hyyypertool/issues/1746))
- Un champ éditable a été ajouté pour le motif de refus dans la modale de refus, permettant une plus grande précision. ([#1718](https://github.com/proconnect-gouv/hyyypertool/issues/1718))
- Ajout de badges de comptage avec emojis pour les sections de la table des utilisateurs. ([#1716](https://github.com/proconnect-gouv/hyyypertool/issues/1716))
- Ajout d'une colonne "Type de vérification" à la table des organisations. ([#1713](https://github.com/proconnect-gouv/hyyypertool/issues/1713))
- La table des utilisateurs affiche désormais une colonne "Interne". ([#1717](https://github.com/proconnect-gouv/hyyypertool/issues/1717))

### Évolutions techniques
- Refactorisation du composant `MemberRowActions` pour le rendre réutilisable. ([#1714](https://github.com/proconnect-gouv/hyyypertool/issues/1714))
- Mises à jour de nombreuses dépendances (TypeScript, Cypress, Hono, etc.) pour améliorer la sécurité et les performances.

### Autres changements
- Amélioration de la formulation du bouton de révocation d'identité. ([#1737](https://github.com/proconnect-gouv/hyyypertool/issues/1737))
- Ajout de notes de publication pour la correction de l'ouverture des PDF des dirigeants d'association.
