## Changelog : tchap-x-ios (30 derniers jours, au 01 juin 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à l'application Tchap X iOS, notamment la possibilité de créer des salons privés non chiffrés, la gestion des comptes expirés et l'optimisation de la résolution des images. Des corrections de bugs ont également été implémentées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- **Salons privés non chiffrés:** Ajout de la possibilité de créer des salons privés non chiffrés, accessible via les "Labs" pour la production. [#341](https://github.com/tchapgouv/tchap-x-ios/pull/341)
- **Gestion des comptes expirés:** L'application gère désormais correctement les comptes expirés, améliorant la sécurité et l'expérience utilisateur. [#344](https://github.com/tchapgouv/tchap-x-ios/issues/344)
- **Optimisation de la résolution des images:** Amélioration de la résolution des images optimisées pour une meilleure qualité visuelle. [#350](https://github.com/tchapgouv/tchap-x-ios/issues/350)
- **Effacement du cache:** Ajout d'une option pour effacer le cache dans les paramètres avancés, permettant de libérer de l'espace et potentiellement résoudre certains problèmes. [#348](https://github.com/tchapgouv/tchap-x-ios/issues/348)
- **Correction de bug - Salons directs:** Correction d'un bug empêchant l'affichage correct des salons directs lorsque l'ID utilisateur provient d'une autre instance Matrix. [#349](https://github.com/tchapgouv/tchap-x-ios/issues/349)

### Évolutions techniques
- **Suppression d'un paramètre obsolète:** Suppression du paramètre `accessRuleOverride` pour simplifier la configuration et le code. [#343](https://github.com/tchapgouv/tchap-x-ios/issues/343)
- **Activation des salons privés chiffrés en pré-production:** Activation des salons privés chiffrés en environnement de pré-production.
- **Traduction des titres des notes de publication:** Traduction des titres des notes de publication en français.

### Autres changements
- Incrémentation de la version de l'application.
