## Changelog : docteur-proconnect (30 derniers jours, au 12 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la robustesse et à l'expérience utilisateur de Docteur ProConnect, notamment en corrigeant des problèmes liés à l'authentification OIDC et en améliorant la présentation visuelle. L'application a également été migrée vers un runtime Bun natif pour une meilleure performance sur l'environnement de production.

### Évolutions fonctionnelles
- Correction d'un problème de redirection après authentification OIDC, assurant un retour correct à la page d'accueil après le login. [#67](https://github.com/proconnect-gouv/docteur-proconnect/issues/67)
- Amélioration de la présentation visuelle avec un affichage de type "cowboy shot" pour garantir que le pied de page reste visible, même sur les pages courtes.
- Implémentation de pages d'erreur DSFR personnalisées pour les cas d'erreur 404, 500 et les problèmes d'authentification.
- Amélioration de la journalisation des états d'authentification anormaux, incluant la chaîne complète des erreurs pour faciliter le débogage.

### Évolutions techniques
- Migration vers un runtime Bun natif sur l'environnement Scalingo-24, améliorant les performances et l'efficacité de l'application. [#66](https://github.com/proconnect-gouv/docteur-proconnect/issues/66)
- Correction de plusieurs problèmes liés à la configuration OIDC :
    - Suppression de l'algorithme `userinfo` par défaut dans le fichier `.env`.
    - Envoi de l'URL de redirection publique lors de l'échange de jetons.
    - Suppression du scope `siren`, non autorisé pour ce client.

### Autres changements
- Mise à jour de dépendances :
    - Morgan (1.10.1 -> 1.11.0) [#64](https://github.com/proconnect-gouv/docteur-proconnect/issues/64)
    - Diverses mises à jour de patches. [#65](https://github.com/proconnect-gouv/docteur-proconnect/issues/65)
    - EJS (5.0.2 -> 6.0.1) [#62](https://github.com/proconnect-gouv/docteur-proconnect/issues/62)
    - QS (6.14.2 -> 6.15.2) [#61](https://github.com/proconnect-gouv/docteur-proconnect/issues/61)
