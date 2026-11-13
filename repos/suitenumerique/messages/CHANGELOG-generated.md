## Changelog : messages (30 derniers jours, au 12 novembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'amélioration de l'expérience mobile (iOS et Android), la gestion du stockage et le renforcement de la sécurité. Les utilisateurs bénéficient désormais de nouvelles jauges de stockage et de fonctionnalités de purge, tandis que l'importation de données historiques (PST et IMAP) a été considérablement fiabilisée. L'application mobile est également en phase de préparation pour sa soumission sur l'App Store.

### Évolutions fonctionnelles
- **Gestion du stockage :** Ajout d'une jauge de stockage et d'une logique de purge automatique pour la corbeille et les spams. Les boîtes mail sans quota sont désormais évaluées par rapport au quota de leur domaine.
- **Expérience Mobile :** 
    - Amélioration de l'interface sur iOS et Android (gestion du clavier, barre d'outils de composition, réponse au tap unique sur les dossiers).
    - Déchiffrement des aperçus de notifications sur mobile pour une meilleure confidentialité.
    - Préparation technique de l'application iOS pour la revue de l'App Store.
- **Notifications :** Amélioration de la sécurité avec l'envoi de notifications push chiffrées et l'affichage des aperçus via les web push.
- **Importation de données :** Amélioration de la fiabilité de l'importation des fichiers PST (Outlook) et des comptes IMAP (notamment Orange) pour une meilleure gestion des contacts, des dates et des structures de dossiers.
- **Interface Utilisateur (Web) :** 
    - Ajout de bannières pour signaler l'activation d'une réponse automatique ou un message de service.
    - Pagination de la vue des métriques d'utilisation [#832](https://github.com/suitenumerique/messages/issues/832).
    - Corrections diverses sur la fenêtre de composition et l'affichage des menus déroulants [#850](https://github.com/suitenumerique/messages/issues/850).
- **Authentification (Keycloak) :** Intégration du thème `lst-dsfr` avec l'apparence ProConnect et ajout de nouvelles options de déploiement.

### Évolutions techniques
- **Sécurité et Infrastructure :** 
    - Mise à jour de Caddy [#859](https://github.com/suitenumerique/messages/issues/859) et rafraîchissement des images de base Docker et des certificats CA [#829](https://github.com/suitenumerique/messages/issues/829).
    - Utilisation de valeurs sécurisées pour les paramètres sensibles.
    - Amélioration de la santé du système (healthcheck) via l'utilisation de l'IP du conteneur [#822](https://github.com/suitenumerique/messages/issues/822).
- **Backend & SMTP :** Refactorisation majeure du composant `pymta` pour renforcer la sécurité et la robustesse du code [#857](https://github.com/suitenumerique/messages/issues/857).
- **CI/CD & Tests :** 
    - Optimisation des pipelines de build Docker et de la publication des images (prévention des conflits de push concurrents).
    - Amélioration de la stabilité des tests E2E (Playwright).
- **Refactoring Frontend :** Modernisation du code TypeScript (utilisation des symboles privés JS) et optimisation du rendu des éléments d'interface (tooltips via portails).

### Autres changements
- **Documentation :** Mise à jour du README [#839](https://github.com/suitenumerique/messages/issues/839) et documentation des paramètres requis pour l'intégration Google Drive.
