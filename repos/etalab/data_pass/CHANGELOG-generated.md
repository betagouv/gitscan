## Changelog : data_pass (30 derniers jours, au 30/09/2026)

### Résumé
Ce mois a été marqué par une amélioration majeure de la robustesse de l'intégration avec l'INSEE et le déploiement de nouveaux parcours dédiés aux établissements d'accueil du jeune enfant (EAJE). Le projet renforce également ses capacités d'interaction avec les API externes et améliore la gestion des notifications pour les partenaires.

### Évolutions fonctionnelles
- **Parcours EAJE** : Mise en place de nouvelles fonctionnalités et d'un système de préfiltrage spécifique pour les demandeurs EAJE, incluant une gestion affinée de la visibilité des formulaires.
- **Tarification et éditeurs** : Intégration de nouveaux éditeurs (CapCreche, Osmia Projects, optiCreche) pour la gestion de la tarification EAJE.
- **Amélioration des API et demandes externes** :
  - Possibilité de pré-remplir les formulaires via l'API [#1788](https://github.com/etalab/data_pass/pull/1788).
  - Mise à jour de la gestion des demandes "API Entreprise" (retrait du responsable de traitement).
  - Personnalisation du cadre juridique pour les produits DINUM.
- **Expérience utilisateur et notifications** :
  - Automatisation des notifications vers le support HubEE lors de la validation de certaines demandes.
  - Amélioration du tunnel de formulaire (gestion des étapes mémorisées et du stepper).
  - Personnalisation des titres de pages d'éligibilité selon l'API concernée.
  - Corrections diverses sur l'affichage des bannières et la redirection après connexion.

### Évolutions techniques
- **Optimisation de l'intégration INSEE** : Refonte complète de la communication avec l'INSEE pour garantir la stabilité du service :
  - Mise en place d'un système de "coupe-circuit" (circuit breaker) et de gestion des débits (rate limiting).
  - Utilisation d'une file d'attente (queue) dédiée pour sérialiser les appels.
  - Amélioration de la gestion des jetons d'authentification et de la reprise sur erreur.
- **Sécurité et Authentification** :
  - Mise à jour des scopes OAuth pour inclure `read_webhooks` par défaut.
  - Renforcement de la validation des adresses IP publiques.
  - Restriction de l'accès `local-sign-in` sur l'environnement de staging [#1855](https://github.com/etalab/data_pass/pull/1855).
- **Infrastructure et CI/CD** :
  - Variabilisation des cibles de déploiement dans les workflows GitHub Actions.
  - Déploiement du watchdog [#1778](https://github.com/etalab/data_pass/pull/1778).

### Autres changements
- Documentation des nouveaux scopes OAuth.
- Normalisation des données de test (apostrophes typographiques).
