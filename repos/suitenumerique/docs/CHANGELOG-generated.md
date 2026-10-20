## Changelog : docs (30 derniers jours, au 2026-10-19)

### Résumé
Ce mois a été marqué par une transition architecturale majeure avec le passage du serveur de collaboration vers YHub, offrant une meilleure stabilité et un support du mode hors-ligne amélioré. L'expérience utilisateur a également été enrichie par de nouvelles options d'export, des raccourcis clavier et une interface plus intuitive, notamment pour la gestion des erreurs et des téléchargements.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** :
  - Ajout de l'option de téléchargement au format Markdown.
  - Introduction de raccourcis clavier pour accéder rapidement au mode présentation.
  - Support du mode hors-ligne pour l'arborescence des documents.
  - Transformation automatique des liens collés en liens internes (interlinks).
  - Possibilité de dupliquer un document via le nouveau serveur de collaboration.
- **Expérience utilisateur et Interface** :
  - Refonte visuelle des pages d'erreur (401, 403 et 404) pour une navigation plus fluide.
  - Amélioration de l'interface de chargement des fichiers (upload loader).
  - Amélioration de la recherche : les résultats peuvent désormais s'ouvrir dans un nouvel onglet via Ctrl/Cmd+clic.
  - Ajout d'indications visuelles pour les raccourcis clavier dans les options de document.
- **Accessibilité** :
  - Amélioration de la navigation dans l'arborescence des documents pour les lecteurs d'écran.
  - Optimisation de l'accessibilité des composants de chargement et des menus d'options.
- **Corrections** :
  - Résolution de problèmes de retour à la ligne lors de l'export de textes longs.
  - Correction de l'affichage de la mise en évidence de la recherche dans les blocs de code.
  - Correction de bugs liés au glisser-déposer sur certains formats d'écran.

### Évolutions techniques
- **Architecture et Collaboration** :
  - Migration majeure du serveur de collaboration (passage de Hocuspocus à YHub).
  - Mise en place d'un mécanisme de migration douce des anciens documents S3 vers YHub.
  - Implémentation d'un mode de repli (fallback) via HTTP polling si les WebSockets sont bloqués.
- **Sécurité** :
  - Renforcement de l'authentification via la publication d'une clé publique JWT sur un endpoint JWKS.
  - Durcissement des contrôles d'accès pour les mentions, les commentaires et les écritures de documents.
  - Vérification des jetons JWT pour les services de conversion.
- **Performance et Résilience** :
  - Mise en cache des décisions d'autorisation pour réduire les appels au backend.
  - Optimisation de la gestion des reconnexions et des réinitialisations de sessions de collaboration.
- **Infrastructure et DevOps** :
  - Migration de YHub-server vers TypeScript.
  - Amélioration des déploiements Kubernetes via les charts Helm (gestion des probes et des ressources).
  - Ajout d'outils de tests de charge complets (scénarios k6 et tableaux de bord Grafana).

### Autres changements
- **Documentation** : Mise à jour importante des guides d'installation (YHub, Kubernetes, Keycloak) et de la documentation d'architecture.
- **Internationalisation** : Amélioration du processus de traduction avec une meilleure intégration de Crowdin et mise à jour des chaînes de caractères.
