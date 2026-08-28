## Changelog : acceslibre (30 derniers jours, au 28 août 2026)

### Résumé
Ce mois-ci, la plateforme a enrichi ses capacités de signalement avec l'intégration des équipements sportifs et a affiné la clarté de ses formulaires pour une meilleure expérience utilisateur. En coulisses, des optimisations importantes ont été réalisées sur la gestion des données, l'automatisation des exports et la sécurité de l'API.

### Évolutions fonctionnelles
- **Nouveaux équipements** : Intégration de la gestion des équipements sportifs dans les détails des modèles et les formulaires de retour utilisateur [#2739](https://github.com/MTES-MCT/acceslibre/issues/2739), [#2773](https://github.com/MTES-MCT/acceslibre/issues/2773), [#2785](https://github.com/MTES-MCT/acceslibre/issues/2785).
- **Amélioration de la clarté** : Correction de la formulation de certaines questions et de fautes de frappe (notamment sur les cabines de douche) pour faciliter la saisie [#2787](https://github.com/MTES-MCT/acceslibre/issues/2787), [#2788](https://github.com/MTES-MCT/acceslibre/issues/2788).
- **Accessibilité** : Corrections apportées aux informations relatives à l'accessibilité [#2786](https://github.com/MTES-MCT/acceslibre/issues/2786).
- **Interface utilisateur** : Correction de l'affichage du modal de signalement et de la page de confirmation de fin de démarche [#2754](https://github.com/MTES-MCT/acceslibre/issues/2754).

### Évolutions techniques
- **Gestion des données** : Mise en place de l'exportation des jeux de données vers S3 avec une politique de rétention automatique (30 jours puis mensuelle) [#2764](https://github.com/MTES-MCT/acceslibre/issues/2764).
- **API & Sécurité** : Possibilité d'associer un utilisateur à une clé API pour un meilleur suivi [#2729](https://github.com/MTES-MCT/acceslibre/issues/2729) et introduction d'un mécanisme de désactivation (kill switch) des fonctionnalités entreprises [#2794](https://github.com/MTES-MCT/acceslibre/issues/2794).
- **Intégrité des données** : Mise à jour automatique de la date de vérification lors de l'édition d'un établissement (ERP) [#2772](https://github.com/MTES-MCT/acceslibre/issues/2772).
- **Importation** : Optimisation de l'importation des données en mode enrichissement uniquement [#2763](https://github.com/MTES-MCT/acceslibre/issues/2763).

### Autres changements
- **Refactoring** : Remplacement de la bibliothèque `bleach` par `nh3` pour le nettoyage du contenu [#2744](https://github.com/MTES-MCT/acceslibre/issues/2744).
- **Nettoyage** : Suppression d'anciens correctifs et de retours anticipés dans le code.
