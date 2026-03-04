## Changelog : roadmaps-faciles (30 derniers jours)

### Résumé
Le projet a connu une période d'évolution très active ces dernières semaines, avec des améliorations significatives de la sécurité, de l'expérience utilisateur et de l'infrastructure. De nouvelles fonctionnalités ont été ajoutées, notamment l'authentification à deux facteurs, l'intégration de fournisseurs OAuth pour la connexion, un éditeur Markdown enrichi avec gestion des images, et des options d'intégration avec d'autres outils comme Notion. L'application est désormais plus robuste grâce à l'ajout de tests complets et d'une meilleure gestion des erreurs.

### Évolutions fonctionnelles
- Ajout de l'authentification à deux facteurs (passkey/OTP/email) et de l'intégration SSO via OAuth2 pour les tenants [#61].
- Implémentation d'un éditeur Markdown enrichi avec la possibilité de téléverser des images via S3 [#93].
- Possibilité d'intégrer des roadmaps dans d'autres sites web grâce à un mode iframe embarquable [#64].
- Amélioration de la page de gestion des tenants avec une interface de type liste GitHub [#60].
- Ajout d'une page de roadmap accessible en dogfooding [#65].
- Amélioration de l'expérience utilisateur du wizard d'intégration [#103].
- Ajout de la possibilité de créer des posts anonymes avec modération et suppression [#32].
- Ajout d'un système de feature flags pour les super-admins [#97].
- Ajout d'un redirect canonique via le domaine de la plateforme [#92].
- Ajout d'un système de journal d'audit (audit log) et d'observabilité [#23].
- Ajout de la gestion des zones DNS [#92].
- Ajout de l'internationalisation (français et anglais) [#21].
- Ajout de la gestion des domaines personnalisés et d'un pont SSO pour l'administration [#20].
- Ajout d'un administrateur root, d'un profil utilisateur et de la gestion des tenants par l'administrateur [#20].

### Évolutions techniques
- Mise en place d'une suite de tests complète avec Vitest et Playwright pour les tests E2E [#63].
- Refonte des emails avec le framework DSFR Mail et react-email [#58].
- Amélioration de la sécurité avec le durcissement de Sentry et l'ajout de PostHog pour le suivi [#98].
- Mise en place d'un système de CI/CD basé sur GitHub Actions et Scalingo avec déploiement basé sur push [#90, #91].
- Utilisation de release-please pour la gestion des releases [#86].
- Suppression de NODE_ENV des fichiers .env pour améliorer la sécurité [#81].
- Filtrage des jobs CI par fichiers modifiés pour optimiser les temps de build [#73].
- Correction de vulnérabilités identifiées par Dependabot (hono, lodash) [#79].
- Adaptation du workflow de travail pour permettre des sessions de développement parallèles avec Claude [#62].

### Autres changements
- Synchronisation de la documentation avec les tickets GitHub et ajout de nouvelles sections sur le workflow, Git, GitHub et la sécurité [#85, #1234].
- Refonte des captures d'écran et de la documentation avec le thème DSFR [#52].
- Ajout de règles pour la création d'issues GitHub [#82].
- Mise à jour du template GitHub [#54].
- Ajout de fichiers ADR (Architecture Decision Records) [#18].
- Mise à jour du fichier `todo.md` [#66, #67].
