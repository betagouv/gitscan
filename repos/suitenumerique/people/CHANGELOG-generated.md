## Changelog : people (30 derniers jours, au 04/11/2026)

### Résumé
Cette période a été marquée par un renforcement de la sécurité des accès et des données, ainsi que par une amélioration de l'interface utilisateur via l'ajout de nouveaux éléments de navigation. L'infrastructure de test et de déploiement a également été largement modernisée pour gagner en fiabilité et en conformité.

### Évolutions fonctionnelles
- **Interface utilisateur** : Ajout d'un pied de page flottant comprenant un formulaire de support et un nouvel élément visuel.
- **Sécurité et permissions** :
  - Restriction de la visibilité de la configuration des domaines pour les utilisateurs disposant de droits de lecture uniquement.
  - Durcissement de la validation des domaines d'e-mails pour les organisations afin d'assurer une correspondance exacte.
- **Internationalisation** : Mise à jour des chaînes de caractères traduites pour améliorer l'expérience multilingue.

### Évolutions techniques
- **CI/CD et Tests** :
  - Modernisation de la chaîne de déploiement via la mise à jour des GitHub Actions (checkout, setup-python, setup-node, cache, etc.) et adoption du preset de configuration par défaut de la Suite Numérique.
  - Mise à jour de Playwright pour optimiser l'exécution des tests automatisés.
- **Sécurité** : Mise à jour de la bibliothèque `urllib3` pour corriger des vulnérabilités.
- **Maintenance et nettoyage** :
  - Suppression du support Crisp.
  - Nettoyage du package `oauth-provider`.
  - Mise à jour du kit d'interface utilisateur (ui-kit).

### Autres changements
- Refactorisation de variables pour assurer la conformité aux standards de qualité de code (Sonar).
