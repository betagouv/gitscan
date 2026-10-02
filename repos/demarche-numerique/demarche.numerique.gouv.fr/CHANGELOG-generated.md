## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 01/10/2026)

### Résumé
Ce mois a été marqué par une montée en puissance de la sécurité et de la résilience du système. Les évolutions majeures concernent l'obligation de passer par ProConnect pour les administrateurs, la mise en place d'un mode "dégradé" pour la saisie des données d'entreprises (SIRET/RNA) en cas d'indisponibilité des API externes, et une refonte profonde de la gestion des sessions. L'expérience des instructeurs a également été fluidifiée par de nouveaux outils de filtrage et une interface plus cohérente.

### Évolutions fonctionnelles
- **Authentification et accès :**
  - Généralisation de l'usage de ProConnect pour les administrateurs et les gestionnaires, avec une gestion stricte des invitations et des accès [#13779](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13779).
  - Renforcement de la sécurité des comptes "Super Admin" via l'enrôlement obligatoire en OTP (code à usage unique) et un verrouillage automatique après plusieurs échecs.
  - Amélioration de la gestion des sessions : expiration basée sur le rôle, enregistrement des sessions utilisateurs et déconnexion automatique lors d'un changement de mot de passe.
- **Résilience des données (SIRET/RNA) :**
  - Introduction d'un mode "dégradé" : en cas d'échec ou d'indisponibilité de l'API Entreprise, l'usager peut désormais poursuivre sa saisie sans être bloqué, avec un suivi spécifique pour l'instructeur.
  - Amélioration de la clarté des messages d'erreur lors de l'utilisation des données externes.
- **Gestion des dossiers et AMI (Appel à Manifestation d'Intérêt) :**
  - Intégration du recueil du consentement usager pour les démarches AMI directement depuis le dossier.
  - Ajout de nouveaux blocs d'information et de suivi du consentement dans l'interface usager.
- **Outils pour les instructeurs :**
  - Amélioration des capacités de filtrage, notamment par périodes de dates pour les colonnes de dossiers.
  - Optimisation de la messagerie et de l'affichage de l'historique des événements d'un dossier.

### Évolutions techniques
- **Architecture et Performance :**
  - Migration vers Sidekiq 8 pour une meilleure gestion des tâches de fond [#13926](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13926).
  - Optimisation des performances de recherche via l'utilisation de `tsvector` et l'indexation des termes de recherche.
  - Amélioration des temps de réponse grâce à un meilleur préchargement (preloading) des données (notices, templates, pièces jointes) dans les vues instructeurs.
- **Sécurité et Robustesse :**
  - Implémentation d'un sandboxing pour le traitement des images (via libvips) afin d'isoler les processus de décodage et protéger le serveur.
  - Renforcement de la validation des URLs et des jetons (JWT) pour les API.
  - Amélioration de la gestion des erreurs des API externes (Commune, Adresse, Entreprise) avec des mécanismes de retry et une meilleure distinction entre panne de service et rejet de jeton.
- **Refactoring :**
  - Migration massive de vues de HAML vers ERB pour une maintenance simplifiée.
  - Création d'un composant `FixedFooterComponent` partagé pour uniformiser les pieds de page des formulaires et modales.
  - Refonte de la gestion des composants de réglages via un nouveau composant `SettingsTileComponent`.

### Autres changements
- **Accessibilité (a11y) :**
  - Nombreuses corrections sur les composants de sélection (combobox/select) pour assurer une meilleure compatibilité avec les lecteurs d'écran.
  - Amélioration de la structure des titres et de la gestion des contrastes dans les notifications et les menus.
- **Documentation et Maintenance :**
  - Mise à jour de la documentation technique (AGENTS.md) et de la FAQ.
  - Nettoyage de code : suppression de nombreuses vues et dépendances obsolètes.
