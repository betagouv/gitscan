## Changelog : tchap-web-v4 (30 derniers jours, au 08/10/2026)

### Résumé
Cette période a été marquée par une amélioration significative de la fluidité de l'authentification, notamment grâce à une meilleure détection des emails externes pour éviter les erreurs de serveur. L'interface utilisateur a également été enrichie avec de nouveaux indicateurs visuels (badges de recommandation, informations TCHAP) et une gestion plus fine de la confidentialité des paramètres de chiffrement.

### Évolutions fonctionnelles

**Authentification et Sécurité**
- Amélioration de la détection des utilisateurs externes lors de l'invitation par email pour éviter les erreurs de serveur et ajout d'une fenêtre d'avertissement.
- Restauration du fonctionnement du SSO (Single Sign-On) sur la version desktop.
- Ajout de messages d'erreur plus explicites lors des échecs d'authentification OIDC.
- Possibilité de masquer ou d'afficher les détails de chiffrement dans les paramètres avancés.

**Interface Utilisateur (UI) et Expérience Utilisateur (UX)**
- Ajout d'un badge de recommandation lors de la création de nouvelles discussions [#1675](https://github.com/tchapgouv/tchap-web-v4/pull/1675).
- Intégration d'informations TCHAP dans la nouvelle liste de discussions [#1682](https://github.com/tchapgouv/tchap-web-v4/pull/1682).
- Le filtre de messages non lus est désormais réglé par défaut sur "tous les messages non lus".
- Correction de l'affichage CSS de la page d'accueil et de la taille des titres.
- Correction de l'ouverture des liens de service "Gaufre".
- Correction du paramètre de masquage du numéro de téléphone [#1666](https://github.com/tchapgouv/tchap-web-v4/pull/1666).

### Évolutions techniques

**Maintenance et Qualité**
- Nettoyage de la suite de tests avec la suppression de Cypress.
- Mise à jour et correction de nombreux tests unitaires, notamment sur la vérification d'email et la gestion des sections de la liste de discussions.
- Amélioration de la CI (Intégration Continue) et du linting du code.

**Optimisations et Corrections**
- Correction d'un bug où les préférences d'analytics de l'utilisateur étaient réinitialisées au redémarrage de l'application [#1687](https://github.com/tchapgouv/tchap-web-v4/pull/1687).
- Refactorisation du composant bouton de l'onglet d'aide.
- Amélioration de la résilience lors de la récupération du serveur d'accueil pour les emails [#1668](https://github.com/tchapgouv/tchap-web-v4/pull/1668).

### Autres changements
- Mise à jour de la documentation (README).
- Corrections liées à l'internationalisation (i18n).
- Ajustements de la configuration (gestion du chiffrement dans les DM, pages intégrées).
