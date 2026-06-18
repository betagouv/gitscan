## Changelog : owuiapps-agents (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'une forte concentration sur la sécurité, avec de nombreuses corrections et améliorations pour protéger les données et l'accès. L'interface utilisateur a également été améliorée avec l'intégration du design system DSFR, une meilleure présentation des informations utilisateur et des améliorations visuelles. De nouvelles fonctionnalités permettent de gérer dynamiquement la liste des modèles d'IA et de se déconnecter correctement des systèmes d'authentification fédérés.

### Évolutions fonctionnelles
- Ajout d'une déconnexion fédérée Keycloak pour une fin de session SSO complète lors de la déconnexion [#54290a0](https://github.com/IA-Generative/owuiapps-agents/commit/54290a0).
- Implémentation d'un chargement dynamique de la liste des modèles d'IA avec un cache et un bouton d'actualisation, ainsi qu'un menu déroulant pour la sélection [#51a04ed](https://github.com/IA-Generative/owuiapps-agents/commit/51a04ed).
- Affichage du nom de l'utilisateur connecté et ajout d'un bouton de déconnexion dans l'en-tête de l'application [#2ceb5c6](https://github.com/IA-Generative/owuiapps-agents/commit/2ceb5c6).
- Uniformisation de l'en-tête et du pied de page avec le design system DSFR pour une cohérence visuelle avec MyVault [#dcebf05](https://github.com/IA-Generative/owuiapps-agents/commit/dcebf05).
- Ajout d'une icône d'application basée sur le rôle de l'utilisateur (agent + badge de création) [#af0f021](https://github.com/IA-Generative/owuiapps-agents/commit/af0f021).
- Ajout d'un logo "Mes Agents" (favicon et en-tête) pour une meilleure identification de l'application [#e1e0a97](https://github.com/IA-Generative/owuiapps-agents/commit/e1e0a97).

### Évolutions techniques
- Mise à jour de `next/postcss/vitest` pour corriger des vulnérabilités de sécurité connues [#a00f16a](https://github.com/IA-Generative/owuiapps-agents/commit/a00f16a).
- Ajout d'une limitation de débit sur les endpoints LLM pour prévenir les abus [#0404672](https://github.com/IA-Generative/owuiapps-agents/commit/0404672).
- Contrôle des valeurs de visibilité et de statut lors de la création d'agents [#1e39c81](https://github.com/IA-Generative/owuiapps-agents/commit/1e39c81).
- Restriction de l'accès au chat d'agent au périmètre autorisé [#39aed2c](https://github.com/IA-Generative/owuiapps-agents/commit/39aed2c).
- Conservation du jeton OIDC côté serveur uniquement pour une sécurité accrue [#9a4b5a9](https://github.com/IA-Generative/owuiapps-agents/commit/9a4b5a9).
- Validation du rôle et limitation des messages transmis au LLM [#90c3427](https://github.com/IA-Generative/owuiapps-agents/commit/90c3427).
- Ajout d'en-têtes de sécurité HTTP pour une meilleure protection [#4480cc5](https://github.com/IA-Generative/owuiapps-agents/commit/4480cc5).
- Masquage des détails d'erreur internes dans les réponses API pour éviter la divulgation d'informations sensibles [#36e9a14](https://github.com/IA-Generative/owuiapps-agents/commit/36e9a14).
- Documentation de l'hypothèse de confiance sur le décodage du jeton [#f47aaa](https://github.com/IA-Generative/owuiapps-agents/commit/f47aaa).

### Autres changements
- Neutralisation des références aux outils d'assistance dans le dépôt pour une meilleure clarté [#5c774ca](https://github.com/IA-Generative/owuiapps-agents/commit/5c774ca).
- Ajout de garde-fous anti-leak pour la sécurité du code [#bd2162a](https://github.com/IA-Generative/owuiapps-agents/commit/bd2162a).
- Ignorer les sauvegardes `.env` (`.env.bak*`, `*.bak-*`) dans le contrôle de version [#78d60c1](https://github.com/IA-Generative/owuiapps-agents/commit/78d60c1).
- Ajout d'un checkpoint avant les correctifs de sécurité [#361b31f](https://github.com/IA-Generative/owuiapps-agents/commit/361b31f).
