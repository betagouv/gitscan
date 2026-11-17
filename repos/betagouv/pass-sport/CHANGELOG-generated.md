## Changelog : pass-sport (30 derniers jours, au 16 novembre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de l'expérience utilisateur via FranceConnect, notamment grâce au pré-remplissage des informations des dossiers. La fiabilité des données a été renforcée par une meilleure gestion des boursiers (Cnous) et des communes, tandis que la sécurité et l'accès au tableau de bord ont été consolidés.

### Évolutions fonctionnelles
- Amélioration du parcours FranceConnect avec le pré-remplissage des informations des dossiers [#694](https://github.com/betagouv/pass-sport/pull/694) et l'ajout de labels pour identifier les dossiers pré-remplis.
- Simplification du parcours pour les boursiers (formulaire à coche unique) et intégration de nouveaux flux de données Cnous [#695](https://github.com/betagouv/pass-sport/pull/695).
- Fiabilisation de la gestion des communes (nouvelles et anciennes communes) [#721](https://github.com/betagouv/pass-sport/pull/721).
- Prise en compte des bénéficiaires AAH pour les équipes de support.
- Évolutions de l'interface utilisateur (UI) du Dossier Numérique et ajustements de la rédaction pour plus de clarté.

### Évolutions techniques
- Refonte et optimisation des pipelines de traitement des Dossiers Numériques (DN).
- Sécurisation de l'accès au tableau de bord via un chemin secret [#671](https://github.com/betagouv/pass-sport/pull/671) et résolution de problèmes de cache et de gestion des erreurs 404.
- Correction de l'envoi des codes communes de naissance vers l'API Particulier.
- Amélioration du suivi des erreurs avec Sentry, en corrigeant le masquage des URLs du tableau de bord [#735](https://github.com/betagouv/pass-sport/pull/735).
- Mises à jour de l'infrastructure technique (Node.js) et durcissement de la sécurité.

### Autres changements
- Mise à jour de la page des mentions légales.
- Ajout de variables d'environnement pour faciliter le développement local.
