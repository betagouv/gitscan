## Changelog : tchap-desktop (30 derniers jours, au 30 avril 2026)

### Résumé
Cette version apporte des améliorations de sécurité, notamment concernant l'ouverture de fichiers, et corrige un problème lié à l'ouverture de l'application depuis la barre des tâches sous macOS. Des améliorations ont également été apportées à la gestion des liens profonds (deep links) et à la publication des versions.

### Évolutions fonctionnelles
- Correction d'une faille de sécurité lors de l'ouverture de fichiers [#206](https://github.com/tchapgouv/tchap-desktop/pull/206).
- L'application s'ouvre/se montre désormais correctement en cliquant sur son icône dans le dock macOS [#202](https://github.com/tchapgouv/tchap-desktop/issues/202).
- Amélioration de l'expérience utilisateur lors du téléchargement de fichiers : ouverture d'une modale et affichage du fichier dans l'explorateur [#061ab1f](https://github.com/tchapgouv/tchap-desktop/commit/061ab1f).
- Possibilité de configurer un lien profond personnalisé via une variable d'environnement [#209](https://github.com/tchapgouv/tchap-desktop/pull/209).

### Évolutions techniques
- Normalisation des noms des assets de publication pour une meilleure cohérence [#205](https://github.com/tchapgouv/tchap-desktop/pull/205) et [#14f9c3cc7](https://github.com/tchapgouv/tchap-desktop/commit/f9c3cc7).
- Suppression de la configuration manuelle des liens profonds sous macOS, simplifiant la gestion et évitant les conflits [#201](https://github.com/tchapgouv/tchap-desktop/pull/201).
- Modification du workflow de publication pour utiliser directement le nom "Tchap" dans le pattern de version [#98be244](https://github.com/tchapgouv/tchap-desktop/commit/98be244).
- Correction du pattern de version dans le workflow de publication [#4bab981](https://github.com/tchapgouv/tchap-desktop/commit/4bab981).

### Autres changements
- Mises à jour vers les versions 4.19.4, 4.19.5 et 4.19.6 [#203](https://github.com/tchapgouv/tchap-desktop/pull/203), [#208](https://github.com/tchapgouv/tchap-desktop/pull/208) et [#211](https://github.com/tchapgouv/tchap-desktop/pull/211).
- Suppression de code commenté inutile [#3632f06](https://github.com/tchapgouv/tchap-desktop/commit/3632f06).
- Amélioration des commentaires et de l'URL du package [#9ecb836](https://github.com/tchapgouv/tchap-desktop/commit/9ecb836).
