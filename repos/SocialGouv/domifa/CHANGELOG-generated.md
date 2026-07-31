## Changelog : domifa (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette version apporte principalement des mises à jour techniques importantes, notamment la migration vers Angular 20 et Node 22, ainsi que des corrections de sécurité et des améliorations de l'infrastructure. Quelques corrections de bugs et améliorations mineures sont également incluses pour l'interface utilisateur et le backend.

### Évolutions fonctionnelles
*   Correction d'un bug empêchant l'ouverture correcte des modales et des images dans le parcours de découverte de l'application.
*   Ajout d'un bouton permettant d'ajouter tous les témoins dans une section spécifique.
*   Correction de l'envoi double de certains emails.
*   Mise à jour des Conditions Générales d'Utilisation (CGU) pour l'année 2026.

### Évolutions techniques
*   Mise à jour majeure de l'application vers Angular 20, incluant des mises à jour des dépendances associées (Angular CLI, CDK, NRx, ngx-matomo, etc.).
*   Mise à jour de Node.js vers la version 22.
*   Refactorisation de l'infrastructure Nginx pour améliorer la sécurité et la performance, notamment en intégrant les en-têtes de sécurité.
*   Migration des builds d'images Docker vers buildkit-operator.
*   Mise à jour de la librairie `typeorm`.
*   Mise à jour de la librairie `pizzip`.

### Autres changements
*   Correction de divers problèmes mineurs dans l'interface utilisateur (suppression de trackers Matomo inutiles, correction de règles de nettoyage de chaînes de caractères).
*   Suppression de données de test obsolètes.
*   Correction d'erreurs liées à la gestion des domaines pour l'envoi d'emails.
*   Nettoyage du code et corrections de formatage.
*   Mise à jour de la documentation.
*   Correction d'une erreur html-sanitize.
*   Ajout de la librairie sentry pour le suivi des erreurs.
*   Ajout de la règle `@angular-eslint/prefer-inject`.
*   Mise à jour de `ngx-charts`.
*   Mise à jour de `dsfr`.
*   Mise à jour de `ngx-countup`.
*   Mise à jour de `ngx-matomo-client`.
