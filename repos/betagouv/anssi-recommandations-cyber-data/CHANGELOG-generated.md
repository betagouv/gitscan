## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 27 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment pour la gestion des collections Albert et des documents. Des corrections ont été apportées pour assurer la cohérence des données et la suppression correcte des documents. La sécurité a également été renforcée avec des mises à jour de dépendances et une configuration plus sécurisée du CI/CD.

### Évolutions fonctionnelles
- Ajout d'un sélecteur de collection pour faciliter le choix de la collection Albert à utiliser. [#8ef4cfb](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/8ef4cfb)
- Possibilité de supprimer des documents. [#72ae2e6](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/72ae2e6)
- Correction de la sélection de collection : l'application utilise maintenant la collection sélectionnée dans l'interface utilisateur pour lister les documents. [#1e50ca6](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/1e50ca6)
- Ajout de la possibilité d'ajouter un document à partir d'une URL. [#e47f117](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/e47f117)
- Amélioration de la gestion des collections : affichage de l'identifiant de la collection dans la liste déroulante pour distinguer les collections homonymes. [#cb3f42d](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/cb3f42d)
- Ajout d'un formulaire pour récupérer les collections Albert désirées. [#5787f18](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/5787f18)
- Ajout d'une route API pour récupérer les collections Albert disponibles. [#4217447](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/4217447)
- Redirection vers le TDB après authentification. [#f2ab570](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/f2ab570)

### Évolutions techniques
- Correction de la suppression des documents : suppression du document miroir dans la collection Jeopardy lors de la suppression d'un MSC. [#fea161f](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/fea161f)
- Refactorisation du code pour extraire un composant `PageInformationsCollections`. [#acf723a](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/acf723a)
- Mise à jour de la dépendance Docling vers une version >= 2.97.0 pour des raisons de sécurité. [#a8d9e8e](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/a8d9e8e)
- Amélioration de la sécurité du CI/CD : désactivation des identifiants `git` des dépôts clonés et ajout de `zizmor` pour valider la configuration. [#94041bd](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/94041bd) et [#685a93e](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/685a93e)
- Encodage des noms de documents en UTF-8 pour éviter les problèmes de caractères spéciaux. [#cece025](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/cece025)

### Autres changements
- Correction du formatage du code. [#25d57b7](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/25d57b7)
- Nettoyage du code et amélioration de la lisibilité. [#735f0a7](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/735f0a7)
