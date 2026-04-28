## Changelog : tchap-desktop (30 derniers jours, au 23 avril 2026)

### Résumé
Cette version apporte des améliorations à la gestion des liens profonds (deep links), permettant une configuration plus flexible via des variables d'environnement. Des corrections ont été apportées à l'enregistrement des liens profonds et à l'affichage des notifications. L'application réagit désormais correctement au clic sur l'icône du dock sur macOS. Des mises à jour de version ont également été intégrées.

### Évolutions fonctionnelles
- **Liens profonds (Deep Links):** Possibilité de configurer les liens profonds via des variables d'environnement. [#209](https://github.com/tchapgouv/tchap-desktop/pull/209)
- **macOS:** L'application s'ouvre ou se montre correctement lorsque l'icône du dock est cliquée. [#202](https://github.com/tchapgouv/tchap-desktop/issues/202)
- **Notifications:** Correction d'un problème lié à l'affichage des notifications, incluant l'ajout des images de badge. [#192](https://github.com/tchapgouv/tchap-desktop/pull/192)

### Évolutions techniques
- **Workflow:** Amélioration du workflow de publication pour une meilleure gestion des noms de versions. [#208](https://github.com/tchapgouv/tchap-desktop/pull/208), [#197](https://github.com/tchapgouv/tchap-desktop/pull/197)
- **Deep Links:** Refonte de l'enregistrement des liens profonds pour assurer une compatibilité accrue. [#197](https://github.com/tchapgouv/tchap-desktop/pull/197)
- **Développement:** Utilisation de GitHub pour la branche de développement.
- **Suppression de code commenté:** Suppression de code inutile.

### Autres changements
- Mise à jour de la version de l'application à 4.19.6, 4.19.5, 4.19.4 et 4.19.3.
- Ajout des permissions d'overlay icon.
- Normalisation des noms des assets de publication.
- Rétrogradation d'une modification concernant la configuration des liens profonds sur macOS.
