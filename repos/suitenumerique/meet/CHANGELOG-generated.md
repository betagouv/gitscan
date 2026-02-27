## Changelog : meet (30 derniers jours)

### Résumé
Les dernières mises à jour de Meet se concentrent sur l'amélioration de l'accessibilité, la sécurité et la performance. Des correctifs ont été apportés pour améliorer l'expérience utilisateur pour les personnes utilisant des technologies d'assistance, et des mesures de sécurité ont été renforcées pour protéger les données et les applications. Des optimisations de performance ont également été apportées, notamment au niveau de l'administration et des requêtes en base de données.

### Évolutions fonctionnelles
- Ajout d'un onglet de configuration des raccourcis clavier (#975).
- Possibilité d'exposer un lien vers l'application Windows (#976).
- Ajout d'un lien cliquable vers les paramètres généraux dans la fenêtre d'inactivité (#974).
- Amélioration des annonces pour les actions d'épinglage/désépinglage avec un lecteur d'écran (#922).
- Ajout d'annonces globales pour les lecteurs d'écran (#922).
- Support des touches Shift et Alt pour la création de raccourcis (#975).
- Ajout de raccourcis supplémentaires pour améliorer l'accessibilité (#975).
- Localisation du support pour le texte de contexte de la transcription (#1010).

### Évolutions techniques
- Mise à jour de Django pour corriger plusieurs vulnérabilités de sécurité critiques (#954).
- Refactorisation de l'API externe pour améliorer la sécurité et la maintenabilité (#1006).
- Amélioration des performances de l'interface d'administration pour les enregistrements (#954).
- Optimisation des requêtes en base de données dans l'interface d'administration (#954).
- Utilisation d'une image de base Alpine pour le microservice de résumé, améliorant la sécurité et réduisant la taille de l'image (#987).
- Mise à jour des dépendances frontend (tanstack, panda, i18next, vite, livekit) (#1011, #1021).
- Mise à jour des dépendances Python (#1011).
- Suppression de `pip` dans les images de production et des agents pour renforcer la sécurité (#987).
- Epinglage de la version de LiveKit pour correspondre à la production (#1021).
- Ajout de support pour la plateforme ARM64 dans les builds Docker (#87b9ca2).
- Mise à jour des actions GitHub pour utiliser les dernières versions (#117677b).
- Refactorisation des tests d'API externes (#1011).
- Amélioration de la gestion des scopes d'authentification (#1021).
- Ajout de tests pour exposer les failles de permission dans l'API externe (#1021).
- Mise à jour de la configuration par défaut de Renovate (#1011).
- Epinglage de Django à une version inférieure à 6.0.0 (#1011).

### Autres changements
- Correction d'un bug empêchant la mise à jour des préférences de langue allemande (#1021).
- Correction d'un bug lié au support des caractères spéciaux dans le Makefile (#602bcf3).
- Correction de l'indentation dans le fichier Tilt (#1021).
- Mise à jour de la documentation pour Scalingo (#957).
- Correction de fautes de frappe dans la documentation (#1021).
- Mise à jour des termes juridiques (#1021).
- Ajout de permissions en lecture seule pour le CI (#ddb8176).
- Suppression de `curl` de l'image de production frontend (#987).
- Correction d'un bug dans l'ordre de désinstallation de `pip` (#987).
- Correction d'un problème de substitution de variable d'environnement dans Docker Compose (#1021).
- Ajout d'un exemple de génération de clé API avec OpenSSL (#1021).
- Ajout du switch `-p` à la commande `mkdir` dans la documentation (#1021).
- Mise à jour du changelog (#1021).
- Correction d'un problème de rendu GitHub dans la documentation Docker Compose (#1009).
- Ajout de la prise en charge du focus ring sur les composants de conteneur d'onglet (#1012).
- Amélioration de l'accessibilité du bouton de retour (#931).
- Ajout d'un fallback pour le spinner en mode "reduced motion" (#931).
- Correction des labels d'accessibilité pour les tooltips (#910).
- Suppression d'un helper redondant pour le formatage des labels longs (#1011).
- Renommage du répertoire "wellknown" en "well-known" (#1009).
- Ajout de tests pour les notifications (#1021).
