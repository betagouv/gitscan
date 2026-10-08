## Changelog : people (30 derniers jours, au [date])

### Résumé
Cette période est marquée par une simplification majeure de l'application avec le retrait des fonctionnalités liées à OAuth2 et aux fournisseurs d'identité (IdP). La sécurité a été renforcée concernant la gestion des domaines d'e-mails et l'environnement de développement frontend a été modernisé.

### Évolutions fonctionnelles
- **Sécurité** : Renforcement de la vérification des domaines d'e-mails des organisations pour assurer une correspondance exacte.
- **Authentification** : Suppression des fonctionnalités liées à OAuth2 et aux fournisseurs d'identité (IdP).

### Évolutions techniques
- **Base de données** : Nettoyage des tables obsolètes suite au retrait des fonctionnalités OAuth2.
- **Frontend** : Modernisation de la chaîne de qualité avec le passage à ESLint 9 et la transformation de la configuration en plugin.
- **Configuration** : Mise à jour des configurations applicatives pour Desk, l'internationalisation (i18n) et les tests E2E.

### Autres changements
- **Qualité du code** : Refactoring de variables pour assurer la conformité avec les standards Sonar.
