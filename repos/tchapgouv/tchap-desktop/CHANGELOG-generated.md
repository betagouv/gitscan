## Changelog : tchap-desktop (30 derniers jours, au 15 avril 2026)

### Résumé
Cette version apporte des améliorations à la gestion des liens profonds (deeplinks) et des notifications, ainsi que des corrections pour assurer une meilleure expérience utilisateur sur macOS. Plusieurs mises à jour de version ont été publiées, incluant des correctifs et des améliorations internes.

### Évolutions fonctionnelles
- **macOS :** Correction du comportement de l'application lors d'un clic sur l'icône dans le dock. L'application s'ouvre ou se montre désormais correctement [#202](https://github.com/tchapgouv/tchap-desktop/issues/202).
- **Notifications :** Ajout des images manquantes pour les badges de notification [#192](https://github.com/tchapgouv/tchap-desktop/issues/192).
- **Liens profonds (Deeplinks) :** Correction de l'enregistrement des liens profonds pour assurer leur fonctionnement correct [#197](https://github.com/tchapgouv/tchap-desktop/issues/197).

### Évolutions techniques
- **Workflow CI/CD :** Amélioration du workflow de publication pour utiliser directement le nom "Tchap" dans le pattern de version.
- **Normalisation des assets :** Normalisation des noms des assets de publication pour une meilleure cohérence.
- **Reversion :** Restauration de la configuration par défaut des liens profonds sur macOS, suite à un problème rencontré [#201](https://github.com/tchapgouv/tchap-desktop/issues/201).

### Autres changements
- Mise à jour de la version de l'application à 4.19.2, 4.19.3, 4.19.4 et 4.19.5.
- Ajout de permissions pour les icônes d'overlay.
- Mise à jour de la branche de gestion des notifications.
