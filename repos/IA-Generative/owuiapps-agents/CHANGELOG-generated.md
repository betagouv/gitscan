## Changelog : owuiapps-agents (30 derniers jours, au 21 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la sécurité de l'application, avec l'implémentation de protections contre les injections de prompt et l'amélioration de la gestion des vulnérabilités. Des améliorations significatives ont également été apportées à l'interface utilisateur, notamment l'harmonisation avec le design system DSFR et l'ajout de fonctionnalités pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- **Sécurité :** Implémentation d'une garde anti-prompt-injection en profondeur (OWASP LLM01) [#1](https://github.com/IA-Generative/owuiapps-agents/pull/1).
- **Sécurité :** Ajout de messages de blocage clairs et d'une validation obligatoire des instructions pour renforcer la sécurité.
- **Sécurité :** Intégration de détecteurs d'anomalies NeMo pour identifier les comportements suspects.
- **Sécurité :** Mise en place de limitations de débit sur les endpoints LLM pour prévenir les abus.
- **Authentification :** Déconnexion fédérée Keycloak pour une gestion SSO complète.
- **Interface utilisateur :** Uniformisation de l'en-tête et du pied de page avec le design system DSFR pour une cohérence visuelle.
- **Interface utilisateur :** Ajout d'une icône d'application basée sur le rôle de l'utilisateur (agent avec badge de création).
- **Interface utilisateur :** Affichage du nom de l'utilisateur connecté et d'un bouton de déconnexion dans l'en-tête.
- **Modèles :** Chargement dynamique de la liste des modèles avec un cache et un bouton d'actualisation.

### Évolutions techniques
- **Sécurité :** Mise à jour de Next.js vers la version 15.5.19 pour corriger des vulnérabilités de sécurité critiques.
- **Sécurité :** Override des dépendances transitives vulnérables pour renforcer la sécurité de l'application.
- **CI/CD :** Remplacement de l'action Gitleaks v2 par le binaire Gitleaks pour une détection plus efficace des secrets.
- **Tests :** Exclusion des spécifications Playwright du glob Vitest pour optimiser les performances des tests.
- **Architecture :** Réorganisation de l'arborescence du dépôt et création d'une carte du dépôt pour une meilleure organisation du code.
- **Sécurité :** Isolation de la garde anti-prompt-injection en un composant réutilisable.

### Autres changements
- Suppression des références aux outils d'assistance du dépôt.
- Suppression des mentions d'outils d'assistance du code.
- Ajout de garde-fous anti-leak pour protéger les données sensibles.
- Ignorer les sauvegardes .env (.env.bak*, *.bak-*) dans le système de contrôle de version.
- Documentation de l'hypothèse de confiance sur le décodage du jeton.
- Ajout d'en-têtes de sécurité HTTP pour renforcer la sécurité de l'application.
- Masquage des détails d'erreur internes dans les réponses API pour éviter de divulguer des informations sensibles.
- Restriction de l'accès au chat d'agent au périmètre autorisé.
- Contrôle des valeurs de visibilité et de statut lors de la création d'agents.
- Validation du rôle et limitation des messages transmis au LLM.
- Conservation du jeton OIDC côté serveur uniquement.
