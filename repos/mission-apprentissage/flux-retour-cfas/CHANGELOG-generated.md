## Changelog : flux-retour-cfas (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur avec l'ajout de nouvelles pages d'atterrissage, l'activation progressive de la version 2 pour la collaboration et la déclaration, ainsi que des corrections de bugs pour assurer la stabilité de la plateforme. Des améliorations de la chaîne de déploiement et de la sécurité ont également été apportées.

### Évolutions fonctionnelles
- Ajout de pages d'atterrissage pour l'inscription et l'information générale [#4602].
- Affichage des effectifs de moins de 16 ans comme "hors champ" dans le tableau des CFA [#4607].
- Ajout d'un indicateur de collaboration sur l'interface [#4609].
- Correction des liens vers les pages d'atterrissage dans le footer [#4608].
- Activation de la version 2 de la collaboration et de la déclaration pour 10 CMA de Nouvelle-Aquitaine [#4597] et 7 CMA de Hauts-de-France [#4590].
- Intégration de Crisp pour le support utilisateur sur la page des CFA [#4596].
- Prise en compte de la date correcte pour l'ouverture des collaborations [#4591].

### Évolutions techniques
- Migration de l'outil de détection de secrets de Talisman vers Gitleaks [#4600].
- Amélioration de la chaîne de déploiement pour une meilleure homogénéisation [#4598].
- Correction d'erreurs de déduplication des enregistrements de Machine Learning [#4601, #4599].
- Ajout d'un endpoint d'activation v2 [#4606].
- Gestion des déclarations de rupture d'apprentissage pour les organismes inter-régions [#4605].
- Adaptation des statistiques pour la collaboration [#4595].
- Correction de bugs dans le fichier `release.yml` pour améliorer le processus de publication [#4604, #4603].

### Autres changements
- Ajout de Lucas en tant qu'utilisateur autorisé [#4593, #4592].
- Mise à jour des habilitations pour certains utilisateurs [#4594].
- Correction de vulnérabilités de sécurité identifiées par Dependabot [#4610].
