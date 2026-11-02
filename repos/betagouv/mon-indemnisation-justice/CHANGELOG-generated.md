## Changelog : mon-indemnisation-justice (30 derniers jours, au 30/10/2026)

### Résumé
Ce mois a été marqué par une amélioration significative de la flexibilité du parcours usager, notamment grâce à la possibilité de modifier une déclaration après sa soumission. En parallèle, l'infrastructure a connu une modernisation majeure avec le passage à FrankenPHP, visant à optimiser la performance et la fiabilité des déploiements.

### Évolutions fonctionnelles
- **Gestion des déclarations** : Possibilité d'éditer une déclaration déjà soumise, avec renvoi automatique de l'email de confirmation si l'adresse du requérant est modifiée [#205](https://github.com/betagouv/mon-indemnisation-justice/pull/205).
- **Outils pour les agents** : Amélioration de la gestion des dossiers avec la possibilité de réattribuer une déclaration via une modale, correction de l'auto-affectation et uniformisation des avis d'intervention pour les agents FDO.
- **Suivi et visibilité** : Affichage de l'état de la déclaration et tri des dossiers par date du dernier changement de statut pour faciliter le pilotage.
- **Parcours usager et authentification** : Correction du processus de création de compte par invitation via FranceConnect et amélioration de la clarté des messages d'erreur.
- **Expérience utilisateur** : Nettoyage de l'interface rédacteur (retrait de Crisp) et gestion plus fine des états de brouillon.

### Évolutions techniques
- **Infrastructure et Déploiement** : Migration complète vers **FrankenPHP** pour le déploiement et simplification de l'usage de Docker, désormais limité à l'environnement de développement.
- **Sécurité** : Renforcement de la sécurité des téléchargements (en-têtes sécurisés), validation du contenu des pièces jointes et masquage des en-têtes HTTP sensibles via la configuration Caddy.
- **CI/CD et Tests** : Optimisation des pipelines de tests (annulation des tests en cas de commit sur la même branche, installation directe de `poppler-utils`) et automatisation de la gestion des dépendances.
- **Architecture** : Simplification de la normalisation des objets d'échange et création de vues de base de données via des migrations.

### Autres changements
- Ajout d'un fichier `.gitguardian.yaml` pour la gestion des scans de sécurité.
- Mise à jour de la documentation et des textes de l'interface.
