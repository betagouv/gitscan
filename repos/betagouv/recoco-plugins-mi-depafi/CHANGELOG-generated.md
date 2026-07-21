## Changelog : recoco-plugins-mi-depafi (30 derniers jours, au 20 juillet 2026)

### Résumé
Ce changelog couvre une période d'améliorations significatives pour le plugin recoco-plugins-mi-depafi. Les principales évolutions concernent la gestion des autorisations, la traçabilité des actions, l'interface utilisateur et l'expérience administrateur. Des corrections de bugs et des améliorations de la documentation ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité pour les administrateurs de voir les boutons d'édition et de suppression des réalisations. [#30](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/30)
- Amélioration de l'affichage du contenu des cartes de réalisation. [#39](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/39)
- Ajout d'un sélecteur de recherche pour faciliter la sélection des réalisations lors de la création. [#37](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/37)
- Ajout d'un champ "auteur" pour suivre l'origine des réalisations et restriction des droits de modification/suppression à cet auteur. [#26](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/26)
- Mise en place d'un système de traçabilité des actions (création, suppression) sur les réalisations. [#34](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/34)
- Ajout de notifications pour les nouveaux projets et réalisations, avec une notification spécifique pour le personnel. [#23](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/23)
- Amélioration de l'affichage des informations des projets dans l'interface d'administration.
- Correction d'un bug empêchant l'activation correcte de l'onglet dans la vue de détail d'une réalisation. [#28](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/28)
- Correction de l'affichage de la visibilité des réalisations lors de leur publication. [#41](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/41)
- Correction pour ne pas notifier l'auteur de la réalisation lors d'une action sur celle-ci. [#33](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/33)

### Évolutions techniques
- Refactoring pour ajouter un système de "feature flags" permettant d'activer/désactiver des fonctionnalités. [#29](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/29)
- Utilisation de `marksafe` pour la gestion de la sécurité et la compatibilité avec le nouveau contrat du core. [#25](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/25)
- Intégration de htmx pour améliorer l'interactivité dans l'interface d'administration. [#27](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/27)
- Amélioration de l'architecture des fichiers statiques (CSS, JS) pour une meilleure organisation.
- Correction de chemin d'accès dans les templates. [#9abab97](https://github.com/betagouv/recoco-plugins-mi-depafi/commit/9abab97)

### Autres changements
- Mise à jour de la documentation d'installation du plugin. [#25](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/25)
- Nettoyage et amélioration du code.
- Suppression de CSS inline et regroupement dans des fichiers CSS dédiés.
- Ajout de commentaires pour améliorer la lisibilité du code.
- Correction de l'ordre de tri des réalisations dans la liste. [#38](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/38)
- Suppression de code inutile.
- Bump de version. [#767a3d7](https://github.com/betagouv/recoco-plugins-mi-depafi/commit/767a3d7)
