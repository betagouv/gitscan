## Changelog : ami-app-ios (30 derniers jours, au 2026-05-21)

### Résumé
Cette version apporte des améliorations à la navigation, notamment le rétablissement du bouton de retour lors de l'accès à des services partenaires et la gestion des liens externes. L'application a également été optimisée pour une meilleure gestion des bannières d'information et des URL spéciales. Des corrections de style et des ajustements techniques ont été effectués pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Le bouton de retour est de nouveau fonctionnel lors de la navigation vers des services partenaires [#82](https://github.com/numerique-gouv/ami-app-ios/pull/82) et [#78](https://github.com/numerique-gouv/ami-app-ios/pull/78).
- L'URL pour accéder aux réglages a été mise à jour [#86](https://github.com/numerique-gouv/ami-app-ios/pull/86).
- Gestion améliorée des liens `mailto` sur les pages partenaires.
- Le bouton de partage des logs a été mis à jour pour correspondre au design de la maquette [#83](https://github.com/numerique-gouv/ami-app-ios/pull/83).
- Les bannières d'information sont de nouveau affichées [#91](https://github.com/numerique-gouv/ami-app-ios/pull/91).
- Suppression du conteneur inutile de bannières dans la vue principale [#93](https://github.com/numerique-gouv/ami-app-ios/pull/93).

### Évolutions techniques
- Introduction d'une classe `AppState` pour gérer l'état de l'application.
- Implémentation d'un `NetworkMonitor` pour surveiller la connectivité réseau et l'intégrer à `AppState`.
- Utilisation d'un `enum` pour détecter les URL web spéciales (suffixe de correspondance) pour une meilleure gestion des liens.
- Refactoring pour gérer correctement les actions de déconnexion de l'utilisateur.
- Utilisation de `Observable` pour la classe `InformationBanner`.
- Amélioration de la gestion des URL racine avec un slash final pour une meilleure compatibilité.
- Correction de problèmes de fusion et de conflits de code.

### Autres changements
- Correction de messages de log incorrects sur les pages partenaires.
- Mise à jour du style du bouton "Partager les logs".
- Suppression de code inutile.
- Utilisation d'un bouton "Retour" personnalisé avec une icône en forme de triangle.
- Remplacement des applications de revue par une liste plutôt que de les ajouter individuellement.
- Affichage du titre de retour en gras.
- Liste des hôtes FI à ne pas traiter comme des partenaires.
