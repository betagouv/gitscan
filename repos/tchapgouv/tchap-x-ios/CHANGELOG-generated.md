## Changelog : tchap-x-ios (30 derniers jours, au 12 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment l'activation de la création de salles privées non chiffrées en mode laboratoire, la gestion des comptes expirés, et l'optimisation de la résolution des images. Des corrections de bugs ont également été implémentées pour améliorer la stabilité et la fiabilité de l'application, ainsi que des améliorations de l'affichage des listes de salles dans les espaces.

### Évolutions fonctionnelles
- **Salles privées non chiffrées :** Possibilité de créer des salles privées non chiffrées via les paramètres "Labs" pour la production. [#341](https://github.com/tchapgouv/tchap-x-ios/pull/341)
- **Gestion des comptes expirés :** L'application gère désormais les comptes expirés. [#344](https://github.com/tchapgouv/tchap-x-ios/issues/344)
- **Optimisation des images :** Amélioration de la résolution des images optimisées. [#350](https://github.com/tchapgouv/tchap-x-ios/issues/350)
- **Cache :** Ajout d'une option pour effacer le cache dans les paramètres avancés. [#348](https://github.com/tchapgouv/tchap-x-ios/issues/348)
- **Invitation DM :** Invitation du destinataire d'un message direct à une nouvelle salle. [#5588](https://github.com/tchapgouv/tchap-x-ios/issues/5588)
- **Affichage des salles :** Correction de l'affichage des listes de salles dans les espaces, notamment pour les utilisateurs provenant d'autres instances. [#5595](https://github.com/tchapgouv/tchap-x-ios/issues/5595)
- **Authentification Tchap Classic :** Connexion à Tchap Classic pour une authentification automatique.
- **Traduction :** Mise à jour des traductions. [#5604](https://github.com/tchapgouv/tchap-x-ios/issues/5604)

### Évolutions techniques
- **Mise à jour du SDK :** Mise à jour du SDK Matrix vers la version 26.05.18.
- **Refactoring OIDC/OAuth :** Correction du refactoring de l'authentification OIDC vers OAuth.
- **Suppression de code inutile :** Suppression d'une méthode non utilisée.
- **Gestion de la pause/reprise du client :** Intégration de la pause et de la reprise du client avec le démarrage et l'arrêt de la synchronisation pour les builds de nuit et de débogage.
- **Correction de conflits de rebase :** Résolution des conflits de rebase lors de l'intégration de ElementX-ios v26.05.3.

### Autres changements
- **Correction visuelle :** Correction d'un problème d'affichage du bandeau supérieur.
- **Correction d'un bug d'affichage :** Correction d'un bug d'affichage du badge d'élément.
- **Traduction des titres :** Traduction des titres des notes de publication en français.
- **Suppression d'un paramètre :** Suppression du paramètre `accessRuleOverride`. [#343](https://github.com/tchapgouv/tchap-x-ios/issues/343)
- **Correction des tests unitaires :** Correction de la construction des tests unitaires.
