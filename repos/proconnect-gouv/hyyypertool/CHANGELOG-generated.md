## Changelog : hyyypertool (30 derniers jours, au 7 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment l'ajout d'un mode sombre et des corrections pour une meilleure lisibilité. Des ajustements ont également été apportés à la gestion des modérations et à la signature des emails. Plusieurs mises à jour de dépendances ont été effectuées pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout du mode sombre pour une expérience utilisateur plus confortable, notamment en basse lumière.
- Suppression du nom et prénom du modérateur dans les emails de refus de modération, améliorant la confidentialité.
- Amélioration de l'interface utilisateur générale, incluant des ajustements visuels et la correction du bouton de copie.
- Correction d'un bug empêchant l'affichage correct de la liste des modérations lorsque le filtre "positif" était ignoré.
- Correction du fonctionnement des boutons de pagination suite à une fuite de `hx-trigger`.
- Ajout du libellé pour la tranche effectif d'une unité légale.
- Amélioration de l'ouverture du menu "trois points".

### Évolutions techniques
- Mise à jour de plusieurs dépendances, incluant TypeScript, Preact, Cypress, Hono, et les plugins associés (release-it-calver-plugin, prettier-plugin-tailwindcss).
- Mise à jour de la librairie d'identité `@proconnect-gouv/proconnect.identite` de la version 5.0.0 à la version 7.0.0.
- Correction d'une fuite de `hx-trigger` qui cassait la pagination.

### Autres changements
- Mises à jour des dépendances de développement et de test.
- Corrections mineures et améliorations de la documentation.
- Ajustements de configuration pour assurer la compatibilité et la performance.
