## Changelog : proconnect-espace-partenaires (30 derniers jours, au 02 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la documentation concernant l'authentification eIDAS et l'ANSSI, ainsi que sur la correction de quelques erreurs et l'optimisation de la gestion des niveaux de sécurité. Une fonctionnalité permettant aux partenaires d'ajouter des collaborateurs a été brièvement implémentée puis annulée en raison de problèmes.

### Évolutions fonctionnelles
- Les partenaires peuvent désormais ajouter des collaborateurs à leur espace. Cette fonctionnalité a été annulée suite à des problèmes et sera réintroduite ultérieurement. [#386](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/386)
- Amélioration de la documentation concernant les niveaux eIDAS pour les fournisseurs de service. [#352](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/352)
- Classification de l'authentification par email et OTP comme MFA faible (eIDAS1-MFA). [#388](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/388)

### Évolutions techniques
- Mise à jour des dépendances : `@babel/core`, `@uuv/playwright`, `actions/checkout`, `form-data`, `esbuild`, `js-yaml`, `proconnect-gouv/federation/api-partner`, `tsx`.
- Remplacement d'une valeur AMR TOTP non standard. [#385](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/385)
- Suppression de la définition de niveau ACR (Authentication Context Reference) dans la documentation, car obsolète. [#369](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/369)
- Suppression d'anciennes adresses IP. [#360](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/360)

### Autres changements
- Amélioration de la documentation eIDAS : ajout de la norme eIDAS aux tables des matières des FS et FI et intégration des distinctions du guide ANSSI. [#362](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/362)
- Suppression de la distinction "géré par l'organisation" pour eIDAS2/eIDAS3 dans la documentation. [#367](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/367)
- Ajout d'un dossier `.idea` au fichier `.gitignore`. [#391](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/391)
- Mise à jour du lien vers le code de calcul du service public. [#384](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/384)
- Correction d'une faute de frappe dans la documentation. [#354](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/354)
- Refactorisation de la documentation eIDAS pour déplacer le contenu partagé vers un dossier `ressources`. [#355](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/355)
