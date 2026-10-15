## Changelog : tchap-web-v4 (30 derniers jours, au 08 octobre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de l'expérience utilisateur dans la gestion des salons et le renforcement de la sécurité lors des interactions avec des utilisateurs externes. L'interface a été affinée pour offrir plus de clarté (notamment sur le chiffrement) et l'authentification a été stabilisée, incluant le rétablissement du SSO sur desktop et l'introduction de la connexion par QR Code.

### Évolutions fonctionnelles
- **Gestion des salons et messages**
  - Amélioration de la liste des salons avec l'ajout d'informations Tchap et l'application d'un filtre par défaut sur les messages non lus.
  - Ajout d'un badge "recommandé" lors de la création de nouveaux salons [#1675](https://github.com/tchapgouv/tchap-web-v4/pull/1675).
- **Sécurité et Authentification**
  - Renforcement de la détection des utilisateurs externes lors des invitations par e-mail avec l'ajout d'une fenêtre d'avertissement pour prévenir les erreurs de saisie de serveur [#1686](https://github.com/tchapgouv/tchap-web-v4/pull/1686).
  - Amélioration de la détection des cibles externes lors des processus d'invitation [#1680](https://github.com/tchapgouv/tchap-web-v4/pull/1680).
  - Restauration du fonctionnement du SSO pour la version desktop.
  - Introduction de la possibilité de se connecter via un QR Code (en Feature Flag).
  - Amélioration de la clarté des messages d'erreur OIDC [#1671](https://github.com/tchapgouv/tchap-web-v4/pull/1671).
- **Interface utilisateur (UI)**
  - Possibilité de masquer ou d'afficher les détails de chiffrement dans les paramètres [#1681](https://github.com/tchapgouv/tchap-web-v4/pull/1681).
  - Mise à jour esthétique de l'interface : amélioration du design des en-têtes et pieds de page (normes DSFR), de la page d'accueil et de la taille des titres.
  - Correction de l'affichage des liens de service sur desktop [#1674](https://github.com/tchapgouv/tchap-web-v4/pull/1674).
  - Correction de la gestion de l'affichage du numéro de téléphone dans les paramètres [#1666](https://github.com/tchapgouv/tchap-web-v4/pull/1666).

### Évolutions techniques
- **Tests et Qualité**
  - Augmentation de la couverture de tests unitaires avec Vitest, notamment sur les composants de vérification d'e-mail, les dialogues d'invitation et les en-têtes de salon.
  - Suppression de Cypress pour alléger la suite de tests.
- **Infrastructure et CI/CD**
  - Optimisation des workflows GitHub Actions et mise à jour de la configuration de la CI.
  - Correction des processus de build (Scalingo).
- **Maintenance et Performance**
  - Correction d'un bug de persistance des valeurs d'analytics après redémarrage de l'application [#1687](https://github.com/tchapgouv/tchap-web-v4/pull/1687).
  - Refactorisation du composant bouton de l'onglet d'aide.
  - Amélioration de la gestion de l'internationalisation (i18n).
  - Nettoyage de fichiers desktop obsolètes.

### Autres changements
- Mise à jour de la documentation (README).
- Intégration de nouvelles informations relatives à Tchap dans l'application [#1682](https://github.com/tchapgouv/tchap-web-v4/pull/1682).
