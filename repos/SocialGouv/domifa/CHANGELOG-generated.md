## Changelog : domifa (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette version apporte principalement des mises à jour techniques importantes, notamment une migration vers Angular 20 et Node 22, ainsi que des améliorations de la sécurité et de l'infrastructure. Quelques corrections de bugs et des ajustements mineurs ont également été effectués sur le frontend et le backend.

### Évolutions fonctionnelles
*   Correction d'un bug empêchant l'ouverture correcte des modales et des images dans l'app tour sur le frontend. [#bf0ddda](https://github.com/SocialGouv/domifa/commit/bf0ddda5aca3abc8175f0e21561c1f8f232d185f)
*   Ajout d'un bouton permettant d'ajouter tous les témoins. [#464f050](https://github.com/SocialGouv/domifa/commit/464f050b62c5b00c4f062ae50e4e2c0cd3e12530)
*   Correction d'un bug lié à l'envoi double de certaines notifications sur le backend. [#f158e0b](https://github.com/SocialGouv/domifa/commit/f158e0b99434681146619257548887f95809d7f4) et [#d15ca38](https://github.com/SocialGouv/domifa/commit/d15ca38479f1f16082f4b9128498687319951651)
*   Mise à jour des conditions générales d'utilisation (CGU) pour l'année 2026.

### Évolutions techniques
*   Mise à jour majeure vers Angular 20 sur le frontend, le portail et l'administration.
*   Mise à jour de Node.js vers la version 22.
*   Refactorisation de l'infrastructure Nginx pour améliorer la sécurité en incluant des en-têtes de sécurité dans chaque bloc de localisation.
*   Migration des builds d'images vers buildkit-operator pour une meilleure performance et fiabilité.
*   Mise à jour de nombreuses dépendances, incluant TypeORM,  @edugouvfr/ngx-dsfr,  ngx-matomo, ngrx et angular cdk.
*   Correction d'erreurs liées à la sanitisation HTML.
*   Suppression de code de test obsolète.

### Autres changements
*   Ajout de Sentry pour la surveillance des erreurs sur le frontend, le portail et l'administration.
*   Amélioration de la configuration et des règles ESLint pour le frontend.
*   Correction de problèmes de formatage des nombres.
*   Mise à jour de la documentation et des fichiers de configuration.
*   Corrections mineures de code et de style.
*   Suppression de commandes meta-psql des dumps de données et de schéma.
