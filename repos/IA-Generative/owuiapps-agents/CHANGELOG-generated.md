## Changelog : owuiapps-agents (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la sécurité et l'amélioration de l'expérience utilisateur de l'application. Des mesures de protection contre les injections de prompts et les fuites de données ont été implémentées, ainsi que des améliorations de l'interface utilisateur pour une meilleure cohérence visuelle et une navigation plus intuitive. Des correctifs de sécurité importants ont également été appliqués en mettant à jour Next.js et ses dépendances.

### Évolutions fonctionnelles
- Ajout d'un garde-fou anti-prompt-injection basé sur les recommandations OWASP LLM01 [#1](https://github.com/IA-Generative/owuiapps-agents/pull/1).
- Implémentation de la déconnexion fédérée Keycloak pour une fin de session SSO complète.
- Chargement dynamique de la liste des modèles d'IA avec un cache et un bouton d'actualisation.
- Affichage du nom de l'utilisateur connecté et d'un bouton de déconnexion dans l'en-tête de l'application.
- Uniformisation de l'en-tête et du pied de page avec le design system DSFR, pour une cohérence avec MyVault.
- Ajout d'une icône d'application basée sur le rôle de l'utilisateur (agent avec un badge "créer").
- Ajout du logo "Mes Agents" comme favicon et dans l'en-tête.

### Évolutions techniques
- Mise à jour de Next.js de la version 14 à la version 15.5.19 pour corriger des vulnérabilités de sécurité critiques.
- Mise à jour de `next/postcss` et `vitest` pour corriger des vulnérabilités connues.
- Ajout de garde-fous anti-leak pour renforcer la sécurité de l'application.
- Ajout d'en-têtes de sécurité HTTP pour une meilleure protection.
- Limitation du débit sur les endpoints LLM pour prévenir les abus.
- Le jeton OIDC est maintenant conservé uniquement côté serveur.
- Validation du rôle et limitation des messages transmis au LLM pour une sécurité accrue.
- Restriction de l'accès au chat d'agent au périmètre autorisé.
- Contrôle des valeurs de visibilité et de statut lors de la création d'agents.

### Autres changements
- Suppression des références aux outils d'assistance dans le code.
- Suppression des mentions d'outils d'assistance du dépôt.
- Ignorer les fichiers de sauvegarde `.env` et `.bak*` dans le contrôle de version.
- Documentation de l'hypothèse de confiance sur le décodage du jeton.
- Masquage des détails d'erreur internes dans les réponses API pour une meilleure sécurité.
- Ajout d'un checkpoint avant les correctifs de sécurité.
