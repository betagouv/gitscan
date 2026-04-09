## Changelog : grist-cw-intra-form (30 derniers jours, au 8 avril 2026)

### Résumé
Ce mois-ci, le projet a connu une refonte significative de l'interface de développement, passant à une implémentation basée sur Vue.js. Cette nouvelle version introduit un éditeur de texte enrichi, des améliorations de la validation des formulaires et des mesures de sécurité renforcées contre les attaques XSS. L'objectif est d'offrir une expérience de développement plus fluide et sécurisée pour les formulaires internes.

### Évolutions fonctionnelles
- Ajout d'un éditeur de texte enrichi pour une saisie plus flexible des données. [#44daa44](https://github.com/gristgouv/grist-cw-intra-form/commit/44daa44)
- Amélioration de la validation des champs de formulaire :
    - La validation de la longueur maximale est désormais appliquée uniquement aux champs de texte et numériques. [#f7c3d11](https://github.com/gristgouv/grist-cw-intra-form/commit/f7c3d11)
    - Correction d'un bug empêchant la fermeture de la fenêtre de validation en cliquant sur la superposition. [#12e99a6](https://github.com/gristgouv/grist-cw-intra-form/commit/12e99a6)
    - Nettoyage des propriétés de champs invalides lors du changement de type de colonne. [#6b0ce15](https://github.com/gristgouv/grist-cw-intra-form/commit/6b0ce15)
- Correction de l'affichage des accents français dans les messages utilisateur. [#f3607df](https://github.com/gristgouv/grist-cw-intra-form/commit/f3607df)

### Évolutions techniques
- Migration vers une version basée sur Vue.js pour l'interface de développement. [#44daa44](https://github.com/gristgouv/grist-cw-intra-form/commit/44daa44)
- Implémentation de DOMPurify pour la sanitisation du contenu HTML, améliorant la sécurité contre les attaques XSS. [#d1bb768](https://github.com/gristgouv/grist-cw-intra-form/commit/d1bb768) et [#fefdc5d](https://github.com/gristgouv/grist-cw-intra-form/commit/fefdc5d)
- Refactoring du code pour améliorer les performances et la lisibilité. [#8c88493](https://github.com/gristgouv/grist-cw-intra-form/commit/8c88493)
- Utilisation de `Vue.toRaw` pour la conversion des Proxies, optimisant la gestion des données. [#d9a15fd](https://github.com/gristgouv/grist-cw-intra-form/commit/d9a15fd)
- Utilisation de `async/await` pour les fonctions appelant `saveConfiguration`, améliorant la gestion des opérations asynchrones. [#9499059](https://github.com/gristgouv/grist-cw-intra-form/commit/9499059)
- Extraction de la fonction `defaultValue` pour une meilleure réutilisabilité du code. [#69d3730](https://github.com/gristgouv/grist-cw-intra-form/commit/69d3730)
- Mise à jour de la source CDN de DOMPurify vers unpkg. [#68b7338](https://github.com/gristgouv/grist-cw-intra-form/commit/68b7338)

### Autres changements
- Amélioration du style de la séparation et du padding dans l'interface de développement. [#f9496b1](https://github.com/gristgouv/grist-cw-intra-form/commit/f9496b1)
- Suppression d'un script JavaScript inutilisé et ajout d'un dossier pour les polices. [#304d42c](https://github.com/gristgouv/grist-cw-intra-form/commit/304d42c)
- Déplacement de la version de développement vers le dossier racine. [#12f6078](https://github.com/gristgouv/grist-cw-intra-form/commit/12f6078)
- Merge de la pull request de test [#50894fe](https://github.com/gristgouv/grist-cw-intra-form/commit/50894fe)
