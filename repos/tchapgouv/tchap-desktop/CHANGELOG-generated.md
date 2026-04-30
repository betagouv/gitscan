## Changelog : tchap-desktop (30 derniers jours, au 23 avril 2026)

### Résumé
Cette version apporte des améliorations à la gestion des liens profonds (deep links), notamment la possibilité de les personnaliser via une variable d'environnement. Des corrections ont également été apportées pour assurer le bon fonctionnement des notifications et de l'ouverture de l'application via l'icône du dock sur macOS. Enfin, plusieurs mises à jour de version ont été déployées.

### Évolutions fonctionnelles
- **Liens profonds:** Possibilité de définir un lien profond personnalisé via une variable d'environnement. [#209](https://github.com/tchapgouv/tchap-desktop/pull/209)
- **macOS:** L'application s'ouvre ou se met au premier plan lorsque l'utilisateur clique sur son icône dans le dock. [#202](https://github.com/tchapgouv/tchap-desktop/issues/202)
- **Notifications:** Correction d'un problème lié aux notifications, avec ajout des images de badge manquantes. [#192](https://github.com/tchapgouv/tchap-desktop/pull/192)

### Évolutions techniques
- **Gestion des assets:** Normalisation des noms des assets de publication pour une meilleure cohérence. [#205](https://github.com/tchapgouv/tchap-desktop/pull/205)
- **Workflow:** Amélioration du workflow de publication pour une meilleure gestion des versions. [#208](https://github.com/tchapgouv/tchap-desktop/pull/208), [#197](https://github.com/tchapgouv/tchap-desktop/pull/197)
- **Deep links:** Correction et refonte de l'enregistrement des liens profonds pour assurer leur fonctionnement sur toutes les plateformes. [#197](https://github.com/tchapgouv/tchap-desktop/pull/197)
- **Configuration macOS:** Suppression de la configuration manuelle des liens profonds sur macOS, puis restauration suite à un problème. [#201](https://github.com/tchapgouv/tchap-desktop/issues/201)

### Autres changements
- Suppression de code commenté inutile.
- Ajout des permissions pour l'icône d'overlay des notifications.
- Mise à jour de la version de l'application à 4.19.6, 4.19.5, 4.19.4 et 4.19.3.
