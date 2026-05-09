## Changelog : ami-app-ios (30 derniers jours, au 7 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à la navigation et à l'expérience utilisateur, notamment la gestion des liens externes, le retour en arrière, et l'intégration d'un nouvel écran d'onboarding pour les notifications. Des corrections de style et des ajustements techniques ont également été effectués pour améliorer la stabilité et la conformité de l'application.

### Évolutions fonctionnelles
- **Gestion des liens :** Prise en charge de l'ouverture des liens `mailto` sur les pages partenaires [#65](https://github.com/numerique-gouv/ami-app-ios/pull/65).
- **Navigation :**
    - Ajout d'un bouton "Retour" sur les pages web externes et partenaires, améliorant la navigation et l'expérience utilisateur [#83](https://github.com/numerique-gouv/ami-app-ios/pull/83), [#78](https://github.com/numerique-gouv/ami-app-ios/pull/78).
    - Amélioration de la gestion du retour à la page d'accueil après avoir effectué un choix concernant les notifications [#76](https://github.com/numerique-gouv/ami-app-ios/pull/76).
    - Navigation vers la page des notifications lors du clic sur une notification push [#59](https://github.com/numerique-gouv/ami-app-ios/pull/59).
- **Onboarding Notifications :** Promotion de la page d'onboarding des notifications en natif, améliorant l'expérience initiale de l'utilisateur [#71](https://github.com/numerique-gouv/ami-app-ios/pull/71).
- **Partage de logs :** Mise à jour du style du bouton de partage de logs pour correspondre aux maquettes [#73](https://github.com/numerique-gouv/ami-app-ios/pull/73), [#72](https://github.com/numerique-gouv/ami-app-ios/pull/72).
- **URL des réglages :** Mise à jour de l'URL d'accès aux réglages [#86](https://github.com/numerique-gouv/ami-app-ios/pull/86).

### Évolutions techniques
- **Architecture :** Introduction d'une classe `AppState` pour gérer l'état de l'application et d'un `NetworkMonitor` pour surveiller la connectivité réseau.
- **Refactoring :**
    - Utilisation de `Observable` pour `InformationBanner`.
    - Déplacement de la `NavigationStack` dans la vue principale de l'application.
    - Création d'une vue `PartnerView` simplifiée pour les pages partenaires.
- **Gestion des URL :** Implémentation d'une logique pour autoriser ou interdire la navigation vers de nouvelles URL via un délégué `WebViewDelegate`.
- **Gestion des partenaires :** Liste des hôtes FI à ne pas traiter comme des partenaires.

### Autres changements
- Correction de messages de log incorrects sur les pages partenaires.
- Amélioration de l'alignement vertical des sous-vues dans la vue d'accueil.
- Correction de typos.
- Mise à jour du style du bouton "Share Logs" pour utiliser le style DSFR.
- Suppression de code inutile.
- Amélioration de la gestion des erreurs de fusion.
