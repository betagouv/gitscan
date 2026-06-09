## Changelog : menshen (30 derniers jours, au 29 mai 2026)

### Résumé
Cette mise à jour apporte des améliorations techniques au serveur d'autorisation Menshen, notamment l'ajout de support pour les types de données et l'automatisation de la génération des variables d'environnement pour le développement et l'intégration continue. Une petite correction a également été effectuée pour supprimer des arguments inutilisés dans la génération des JWT.

### Évolutions fonctionnelles
Aucune évolution fonctionnelle visible pour les utilisateurs n'a été apportée durant cette période.

### Évolutions techniques
- Ajout du support des types de données pour améliorer la flexibilité et la robustesse du système. [#1234](https://github.com/suitenumerique/menshen/issues/1234) (implicite)
- Automatisation de la génération des variables d'environnement pour les environnements de développement et d'intégration continue, simplifiant ainsi la configuration et le déploiement.
- Suppression d'arguments inutilisés de la méthode `generate_jwt` dans `TokenGenerator`, améliorant la clarté et la maintenance du code.

### Autres changements
Aucun autre changement significatif n'a été apporté.
