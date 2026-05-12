## Changelog : tchap-desktop (30 derniers jours, au 7 mai 2026)

### Résumé
Cette version apporte des améliorations de sécurité, notamment concernant l'ouverture de fichiers téléchargés, ainsi que des corrections et des optimisations pour la gestion des liens profonds (deep links) et des mises à jour. L'application est également préparée pour une meilleure gestion des versions et des déploiements.

### Évolutions fonctionnelles
- Correction d'une vulnérabilité de sécurité lors de l'ouverture de fichiers téléchargés. [#206](https://github.com/tchapgouv/tchap-desktop/pull/206)
- Amélioration de la gestion des liens profonds (deep links) avec la possibilité de les personnaliser via des variables d'environnement. [#209](https://github.com/tchapgouv/tchap-desktop/pull/209)
- Modification du comportement de l'action "télécharger" : ouvre une modal et affiche le fichier téléchargé dans l'explorateur de fichiers. [#061ab1f](https://github.com/tchapgouv/tchap-desktop/commit/061ab1f)
- Après téléchargement d'un fichier, l'application affiche maintenant le fichier dans l'explorateur plutôt que de l'ouvrir directement. [#1085f3a](https://github.com/tchapgouv/tchap-desktop/commit/1085f3a)

### Évolutions techniques
- Mise à jour de la version de l'application à 4.19.7. [#217](https://github.com/tchapgouv/tchap-desktop/pull/217)
- Mise à jour des dépendances Cargo. [#3b780e5](https://github.com/tchapgouv/tchap-desktop/commit/3b780e5)
- Amélioration du workflow de publication pour inclure l'upload du fichier `latest.json` pour chaque plateforme. [#7f197a4](https://github.com/tchapgouv/tchap-desktop/commit/7f197a4)
- Création d'un script pour générer le fichier `latest.json` correctement pour chaque plateforme. [#ae61e15](https://github.com/tchapgouv/tchap-desktop/commit/ae61e15)
- Normalisation des noms des assets de release pour une meilleure cohérence. [#205](https://github.com/tchapgouv/tchap-desktop/pull/205)
- Suppression de l'enregistrement manuel des liens profonds sous Windows. [#6ea6a61](https://github.com/tchapgouv/tchap-desktop/commit/6ea6a61)
- Modifications du workflow CI/CD pour une meilleure gestion des versions et des branches. [#98be244](https://github.com/tchapgouv/tchap-desktop/commit/98be244), [#4bab981](https://github.com/tchapgouv/tchap-desktop/commit/4bab981)

### Autres changements
- Mise à jour de la documentation (README). [#e1f9ae7](https://github.com/tchapgouv/tchap-desktop/commit/e1f9ae7)
- Suppression de code commenté. [#3632f06](https://github.com/tchapgouv/tchap-desktop/commit/3632f06)
- Corrections de typos dans les fichiers de configuration. [#4cc39b0](https://github.com/tchapgouv/tchap-desktop/commit/4cc39b0)
- Mise à jour de la version à 4.19.6. [#211](https://github.com/tchapgouv/tchap-desktop/pull/211)
- Mise à jour de la version à 4.19.5. [#208](https://github.com/tchapgouv/tchap-desktop/pull/208)
